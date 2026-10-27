// Odvozené životní údaje z faktů osob (narození, úmrtí, sňatek, místo, domy).
import { people, places } from './data.js';

const parseDate = (f) => {
  const m = f.match(/(?:(\d{1,2})\.\s*(\d{1,2})\.\s*)?(\d{4})/);
  return m ? { y: +m[3], m: +(m[2] || 0), d: +(m[1] || 0), exact: !!m[1], asi: /\basi\b|kolem|cca/.test(f), bound: /před|po\s+\d|nejpozději/.test(f) } : null;
};
const factOf = (p, sym) => (p.facts || []).find((x) => x.trim().replace(/^\d\.\s*/, '').startsWith(sym));
export function birth(p) { const f = factOf(p, '*'); return f ? parseDate(f) : null; }
export function death(p) { const f = factOf(p, '†'); return f ? parseDate(f) : null; }
export function marriage(p) { const f = factOf(p, '×'); return f ? parseDate(f) : null; }
export const ageBetween = (a, b) => b.y - a.y - (a.exact && b.exact && (b.m < a.m || (b.m === a.m && b.d < a.d)) ? 1 : 0);

const stems = places.map((pl) => ({ name: pl.name, stem: pl.name.split(' ')[0].slice(0, Math.max(4, pl.name.split(' ')[0].length - 2)) }));
/** Obec ze známého seznamu míst, která se v textu vyskytuje (poslední výskyt vyhrává). */
export function placeIn(text) {
  let best = null, pos = -1;
  for (const s of stems) { const i = text.lastIndexOf(s.stem); if (i > pos) { pos = i; best = s.name; } }
  return best;
}
export function birthPlace(p) {
  const f = factOf(p, '*');
  if (!f) return null;
  const t = f.split(/[(;]/)[0];
  return placeIn(t);
}

/** Domy (obec + čp.) zmíněné v textu. */
export function housesIn(text) {
  const out = [];
  for (const m of text.matchAll(/čp\.\s*(\d+)/g)) {
    const before = text.slice(Math.max(0, m.index - 70), m.index);
    const place = placeIn(before);
    if (place) out.push({ place, no: m[1] });
  }
  return out;
}
export const houseKey = (h) => `${h.place} čp. ${h.no}`;
export const houseSlug = (h) => (h.place + '-' + h.no).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-');

export const allPeople = Object.values(people);
