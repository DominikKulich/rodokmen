#!/usr/bin/env python3
"""Snímek z digitální badatelny Národního archivu (VadeMeCum, vademecum.nacr.cz) – židovské matriky HBMa/HBM a další.

Použití (z kořene projektu):
  nacr.py <cesta> <zmenseni> <vystup.jpg>
  nacr.py --seznam <soubor.txt> <od> <do> <zmenseni> <slozka>
    cesta     = část adresy za „…/inventare/“, tvar dao/images/<složka>/<uuid>.jpg
                (uuid snímků najdeš v prohlížeči: stránka Zoomify.action – náhledy „…/dao/images/0172/<uuid>.jpg/nahled_maly.jpg“,
                 prohlížeč ukazuje po 10; přepínání stránek select.getScanSelect + jQuery change, nebo odkazy PaginatorMedia…row=N)
    soubor.txt = řádky „<číslo snímku> <složka>/<uuid>“ (např. „66 0172/f245b3a0-…“) – pro hromadné stažení rozsahu
    zmenseni  = 0 plné rozlišení (na čtení a výřez), 1 poloviční, 2 čtvrtinové, 3 náhled
Doména do allowlistu: vademecum.nacr.cz (BEZ www). Obrázkový server neomezuje a cookies nepotřebuje.
Hledání knih: viz reference/portaly.md (Židovské matriky – Národní archiv).
"""
import math, os, re, subprocess, sys, tempfile, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = "https://vademecum.nacr.cz/mrimage/vademecum/zoomify//cz/archives/CZ-100000010/inventare/"


def get(url):
    err = None
    for _ in range(3):
        try:
            return urllib.request.urlopen(url, timeout=30).read()
        except Exception as e:
            err = e
            time.sleep(1)
    raise err


def stahni(cesta, red, out):
    base = BASE + cesta.strip("/")
    x = get(base + "/ImageProperties.xml").decode()
    W, H, T = (int(re.search(fr'{k}="(\d+)"', x).group(1)) for k in ("WIDTH", "HEIGHT", "TILESIZE"))
    dims, w, h = [], W, H
    while True:
        dims.append((w, h))
        if w <= T and h <= T:
            break
        w, h = (w + 1) // 2, (h + 1) // 2
    dims = dims[::-1]
    counts = [math.ceil(a / T) * math.ceil(b / T) for a, b in dims]
    L = max(0, len(dims) - 1 - red)
    w, h = dims[L]
    nx, ny = math.ceil(w / T), math.ceil(h / T)
    start = sum(counts[:L])
    d = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(out)) or ".")
    jobs = [(y, xx, os.path.join(d, f"{y:03d}_{xx:03d}.jpg")) for y in range(ny) for xx in range(nx)]

    def one(j):
        y, xx, f = j
        g = (start + y * nx + xx) // 256
        open(f, "wb").write(get(f"{base}/TileGroup{g}/{L}-{xx}-{y}.jpg"))

    with ThreadPoolExecutor(8) as ex:
        list(ex.map(one, jobs))
    tmp = out + ".tmp.jpg"
    subprocess.run(["magick", "montage", *[j[2] for j in jobs], "-tile", f"{nx}x{ny}", "-geometry", "+0+0",
                    "-gravity", "NorthWest", "-background", "white", tmp], check=True)
    subprocess.run(["magick", tmp, "-crop", f"{w}x{h}+0+0", "+repage", "-quality", "88", out], check=True)
    for j in jobs:                       # úklid (ve složce bez práva mazat jen tiše selže)
        try: os.remove(j[2])
        except OSError: pass
    for f in (tmp,):
        try: os.remove(f)
        except OSError: pass
    try: os.rmdir(d)
    except OSError: pass
    print(out, w, h)


def main():
    a = sys.argv[1:]
    if len(a) == 6 and a[0] == "--seznam":
        _, seznam, od, do, red, slozka = a
        os.makedirs(slozka, exist_ok=True)
        for radek in open(seznam, encoding="utf-8"):
            p = radek.split()
            if len(p) == 2 and int(od) <= int(p[0]) <= int(do):
                stahni(f"dao/images/{p[1]}.jpg", int(red), os.path.join(slozka, f"snimek_{int(p[0]):03d}.jpg"))
    elif len(a) == 3:
        stahni(a[0], int(a[1]), a[2])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
