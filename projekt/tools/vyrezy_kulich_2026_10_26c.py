#!/usr/bin/env python3
"""Výřezy ze SOA Praha eBadatelna (snímky stažené ručně, uloženy v zdroje/skeny_soapraha), 26. 10. 2026.
Spustit z kořene projektu:  python3 tools/vyrezy_kulich_2026_10_26c.py"""
from PIL import Image
J = [
 ("novaves_krest_jan_kulich_1839", "Veprek_15__060.jpg", (0.04, 0.305, 0.965, 0.46)),
 ("novaves_umrti_rozalie_kulichova_1877", "Veprek_28__125.jpg", (0.04, 0.54, 0.985, 0.645)),
 ("zlosyn_krest_anny_1854", "Veltrusy_15__066.jpg", (0.07, 0.27, 0.94, 0.895)),
]
for key, src, (a, b, c, d) in J:
    im = Image.open(f"zdroje/skeny_soapraha/{src}").convert("L")
    w, h = im.size
    full = im.copy(); full.thumbnail((1866, 99999)); full.save(f"zdroje/{key}.jpg", quality=85)
    cr = im.crop((int(a*w), int(b*h), int(c*w), int(d*h)))
    if cr.width > 1800: cr = cr.resize((1800, round(cr.height*1800/cr.width)), Image.LANCZOS)
    cr.save(f"vyrezy/{key}.jpg", quality=85)
    print("ok", key, cr.size)
# doplněno: oddavky Josef Kulich × Rozálie ovdovělá Jindřichová, Nová Ves 15. 1. 1833 (Vepřek 15 sn. 8), box (0.03, 0.165, 0.975, 0.36)
