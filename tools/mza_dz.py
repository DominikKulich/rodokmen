#!/usr/bin/env python3
"""Snímek z Acta Publica (MZA Brno) přes Deepzoom (iipsrv), bez prohlížeče.

Použití: mza_dz.py <kniha-adresář> <číslo snímku> <zmenseni> <vystup.jpg>
  kniha-adresář = např. 216000010-000253-003375-000000-009105-000000-FM-B10312 (z názvu .jp2 bez -NNNNN)
  číslo snímku  = pořadí v knize (1 = …-00010.jp2, 2 = …-00020.jp2 …)
  zmenseni      = 0 plné, 1 poloviční, 2 čtvrtinové
CVT=jpeg server blokuje (403); Deepzoom vyžaduje Referer z actapublica.
Cesta /srv/LUNxxx/… se liší podle knihy: zjisti ji v prohlížeči (požadavek …iipsrv.fcgi?Deepzoom=…dzi) a dej jako env MZA_LUN (výchozí LUN105/LUN105).
"""
import math, os, re, subprocess, sys, tempfile, urllib.request
REF = "https://www.mza.cz/actapublica/matrika/"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130 Safari/537.36"
def get(u):
    # urllib dostane 426 (server chce HTTP/2) -> curl
    for _ in range(3):
        r = subprocess.run(["curl", "-sS", "--fail", "--max-time", "30", "-A", UA, "-e", REF, u], capture_output=True)
        if r.returncode == 0: return r.stdout
    raise RuntimeError(f"stažení selhalo: {u} {r.stderr.decode()[:200]}")
def main():
    if len(sys.argv) != 5: sys.exit(__doc__)
    kniha, n, red, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    luns = [os.environ["MZA_LUN"]] if os.environ.get("MZA_LUN") else [f"LUN{i}/LUN{i}" for i in range(100, 115)]
    x = None
    for lun in luns:  # LUN složku zjisti automaticky (špatná vrací PNG s chybou)
        cesta = f"/srv/{lun}/{kniha[:9]}/{kniha}/{kniha}-{n*10:05d}.jp2"
        base = "https://www.mza.cz/iipsrv/iipsrv.fcgi?Deepzoom=" + cesta
        try:
            b = get(base + ".dzi")
        except RuntimeError:
            continue
        if b[:1] == b"<":
            x = b.decode(); break
    if x is None: sys.exit("snímek nenalezen v žádné LUN složce")
    T = int(re.search(r'TileSize="(\d+)"', x).group(1))
    W = int(re.search(r'Width="(\d+)"', x).group(1)); H = int(re.search(r'Height="(\d+)"', x).group(1))
    L = math.ceil(math.log2(max(W, H))) - red
    w, h = math.ceil(W / 2**red), math.ceil(H / 2**red)
    nx, ny = math.ceil(w / T), math.ceil(h / T)
    d = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(out)))
    from concurrent.futures import ThreadPoolExecutor
    jobs = [(y, xx, os.path.join(d, f"{y:03d}_{xx:03d}.jpg")) for y in range(ny) for xx in range(nx)]
    def one(j):
        y, xx, f = j
        open(f, "wb").write(get(f"{base}_files/{L}/{xx}_{y}.jpg"))
    with ThreadPoolExecutor(8) as ex: list(ex.map(one, jobs))
    files = [j[2] for j in jobs]
    subprocess.run(["magick", "montage", *files, "-tile", f"{nx}x{ny}", "-geometry", "+0+0", "-gravity", "NorthWest", "-background", "white", out + ".tmp.jpg"], check=True)
    subprocess.run(["magick", out + ".tmp.jpg", "-crop", f"{w}x{h}+0+0", "+repage", "-quality", "88", out], check=True)
    for f in files: os.remove(f)
    os.rmdir(d); os.remove(out + ".tmp.jpg")
    print(out, w, h)
if __name__ == "__main__": main()
