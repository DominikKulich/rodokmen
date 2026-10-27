// Shared by the tree on the homepage and the separate tree page.
export function initTree(tree: HTMLElement) {
  const svg = tree.querySelector<SVGSVGElement>('.strom')!;
  const stage = tree.querySelector<HTMLElement>('.strom-wrap')!;
  const readout = tree.querySelector<HTMLOutputElement>('[data-zoom-level]');
  const pointers = new Map<number, { x: number; y: number }>();
  let zoom = 1;
  let suppressClick = false;
  let drag: { x: number; y: number; left: number; top: number } | null = null;
  let pinch: { distance: number; zoom: number; x: number; y: number } | null = null;
  const limit = (value: number) => Math.max(1, Math.min(12, value));
  const point = (x: number, y: number) => {
    const rect = stage.getBoundingClientRect();
    return { x: x - rect.left - stage.clientLeft, y: y - rect.top - stage.clientTop };
  };
  function setZoom(value: number, anchor = { x: stage.clientWidth / 2, y: stage.clientHeight / 2 }, fixed?: { x: number; y: number }) {
    const oldWidth = svg.getBoundingClientRect().width;
    const world = fixed ?? { x: (stage.scrollLeft + anchor.x) / oldWidth, y: (stage.scrollTop + anchor.y) / oldWidth };
    zoom = limit(value);
    svg.style.width = `${stage.clientWidth * zoom}px`;
    const width = svg.getBoundingClientRect().width;
    stage.scrollLeft = world.x * width - anchor.x;
    stage.scrollTop = world.y * width - anchor.y;
    if (readout) readout.value = `${Math.round(zoom * 100)} %`;
    tree.querySelectorAll<HTMLButtonElement>('[data-zoom]').forEach(button => {
      button.disabled = button.dataset.zoom === 'out' ? zoom <= 1 : button.dataset.zoom === 'in' ? zoom >= 12 : false;
    });
  }
  function resetGesture() {
    const [a, b] = [...pointers.values()];
    pinch = null;
    drag = a ? { ...a, left: stage.scrollLeft, top: stage.scrollTop } : null;
    if (a && b) {
      const center = point((a.x + b.x) / 2, (a.y + b.y) / 2);
      const width = svg.getBoundingClientRect().width;
      pinch = { distance: Math.max(1, Math.hypot(b.x - a.x, b.y - a.y)), zoom,
        x: (stage.scrollLeft + center.x) / width, y: (stage.scrollTop + center.y) / width };
      suppressClick = true;
    }
  }
  stage.classList.add('tree-interactive');
  setZoom(1);
  stage.addEventListener('wheel', event => {
    event.preventDefault();
    const delta = event.deltaY * (event.deltaMode === 1 ? 16 : event.deltaMode === 2 ? stage.clientHeight : 1);
    setZoom(zoom * Math.exp(-Math.max(-300, Math.min(300, delta)) * .002), point(event.clientX, event.clientY));
  }, { passive: false });
  stage.addEventListener('pointerdown', event => {
    if (event.button !== 0) return;
    if (!pointers.size) suppressClick = false;
    pointers.set(event.pointerId, { x: event.clientX, y: event.clientY });
    resetGesture();
    if (pointers.size > 1) {
      pointers.forEach((_, id) => stage.setPointerCapture(id));
      stage.classList.add('dragging');
    }
  });
  stage.addEventListener('pointermove', event => {
    if (!pointers.has(event.pointerId)) return;
    pointers.set(event.pointerId, { x: event.clientX, y: event.clientY });
    if (pinch) {
      const [a, b] = [...pointers.values()];
      const center = point((a.x + b.x) / 2, (a.y + b.y) / 2);
      setZoom(pinch.zoom * Math.hypot(b.x - a.x, b.y - a.y) / pinch.distance, center, pinch);
    } else if (drag) {
      const dx = event.clientX - drag.x, dy = event.clientY - drag.y;
      if (!suppressClick && Math.hypot(dx, dy) < 5) return;
      suppressClick = true;
      stage.scrollLeft = drag.left - dx;
      stage.scrollTop = drag.top - dy;
    }
    stage.setPointerCapture(event.pointerId);
    stage.classList.add('dragging');
    event.preventDefault();
  });
  const finish = (event: PointerEvent) => {
    if (!pointers.delete(event.pointerId)) return;
    resetGesture();
    if (!pointers.size) stage.classList.remove('dragging');
    if (stage.hasPointerCapture(event.pointerId)) stage.releasePointerCapture(event.pointerId);
  };
  stage.addEventListener('pointerup', finish);
  stage.addEventListener('pointercancel', finish);
  stage.addEventListener('lostpointercapture', event => {
    // Touch pointers may initially be captured by a link inside the SVG.
    if (event.target === stage) finish(event);
  });
  stage.addEventListener('pointerleave', event => {
    if (!stage.hasPointerCapture(event.pointerId)) finish(event);
  });
  stage.addEventListener('dragstart', event => event.preventDefault());
  stage.addEventListener('click', event => {
    if (suppressClick) { event.preventDefault(); event.stopPropagation(); suppressClick = false; }
  }, true);
  tree.querySelectorAll<HTMLButtonElement>('[data-zoom]').forEach(button => button.addEventListener('click', () => {
    if (button.dataset.zoom === 'fit') {
      setZoom(1);
      stage.scrollLeft = stage.scrollTop = 0;
    } else setZoom(zoom * (button.dataset.zoom === 'in' ? 1.25 : .8));
  }));
  stage.addEventListener('keydown', event => {
    if (event.target !== stage || !['+', '=', '-', '0'].includes(event.key)) return;
    event.preventDefault();
    setZoom(event.key === '0' ? 1 : zoom * (event.key === '-' ? .8 : 1.25));
  });
  tree.querySelector('[data-focus-legion]')?.addEventListener('click', () => {
    const box = svg.viewBox.baseVal;
    setZoom(Math.max(1.5, Math.min(stage.clientWidth / 940, window.innerHeight * .7 / 960) * box.width / stage.clientWidth));
    tree.scrollIntoView({ block: 'start' });
    stage.scrollLeft = Number(tree.dataset.legionX) / box.width * svg.getBoundingClientRect().width - stage.clientWidth / 2;
    stage.scrollTop = Number(tree.dataset.legionY) / box.height * svg.getBoundingClientRect().height - stage.clientHeight / 2;
  });
  tree.querySelectorAll<HTMLButtonElement>('[data-focus-branch]').forEach(button => button.addEventListener('click', () => {
    const box = svg.viewBox.baseVal;
    const width = Number(button.dataset.focusWidth), height = Number(button.dataset.focusHeight);
    setZoom(Math.min(stage.clientWidth / width, window.innerHeight * .66 / height) * box.width / stage.clientWidth);
    tree.scrollIntoView({ block: 'start' });
    stage.scrollLeft = Number(button.dataset.focusX) / box.width * svg.getBoundingClientRect().width - stage.clientWidth / 2;
    stage.scrollTop = Number(button.dataset.focusY) / box.height * svg.getBoundingClientRect().height - stage.clientHeight / 2;
  }));
  // Přepínače zobrazení (rok, místo narození, povolání) – pamatují se v prohlížeči.
  tree.querySelectorAll<HTMLInputElement>('[data-show]').forEach(box => {
    const key = `strom-show-${box.dataset.show}`;
    try { const saved = localStorage.getItem(key); if (saved !== null) box.checked = saved === '1'; } catch {}
    const apply = () => { tree.classList.toggle(`show-${box.dataset.show}`, box.checked); };
    apply();
    box.addEventListener('change', () => { apply(); try { localStorage.setItem(key, box.checked ? '1' : '0'); } catch {} });
  });
  // Celá obrazovka – Fullscreen API, jinak (iPhone) přes fixní překryv.
  const fsButton = tree.querySelector<HTMLButtonElement>('[data-fullscreen]');
  const isFs = () => document.fullscreenElement === tree || tree.classList.contains('tree-fs');
  const syncFs = () => {
    fsButton?.setAttribute('aria-pressed', String(isFs()));
    if (fsButton) fsButton.textContent = isFs() ? '✕ Zavřít celou obrazovku' : '⛶ Celá obrazovka';
    document.documentElement.style.overflow = tree.classList.contains('tree-fs') ? 'hidden' : '';
    requestAnimationFrame(() => setZoom(zoom));
  };
  fsButton?.addEventListener('click', async () => {
    if (isFs()) {
      if (document.fullscreenElement) await document.exitFullscreen().catch(() => {});
      tree.classList.remove('tree-fs');
    } else if (tree.requestFullscreen) {
      await tree.requestFullscreen().catch(() => tree.classList.add('tree-fs'));
    } else tree.classList.add('tree-fs');
    syncFs();
  });
  document.addEventListener('fullscreenchange', syncFs);
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && tree.classList.contains('tree-fs')) { tree.classList.remove('tree-fs'); syncFs(); } });
  window.addEventListener('resize', () => setZoom(zoom));
}
