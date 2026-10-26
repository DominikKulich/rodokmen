#!/usr/bin/env python3
"""Stáhne snímky z SOA Litoměřice a vyřízne zápisy Kulichů nalezené 26. 10. 2026.
Spustit z kořene projektu, až bude dostupný images.soalitomerice.cz:  python3 tools/vyrezy_kulich_2026_10_26.py
Výstup: vyrezy/<klic>.jpg (≤1800 px) a zdroje/<klic>.jpg (celý snímek)."""
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
import soal_zoomify as z
IMG = "https://images.soalitomerice.cz/ximage/matriky/zoomify/cz/archives/CZ-214000010/"
J = [  # klíč, cesta za CZ-214000010/, box (x0,y0,x1,y1 jako podíl šířky/výšky)
 ("cernoucek_oddavky_vaclav_kulich_anna_ticha_1925", "matriky/dao/images/0082/a07cb0c8-b4e0-442d-b6d1-4e36d48fc817.jpg", (0.03,0.668,0.97,0.885)),
 ("krabcice_oddavky_marie_kulichova_1928", "NAD-856/dao/images/0645/792f8e6c-a73c-466c-9177-8a2a3edd83bf.jpg", (0.10,0.44,0.98,0.80)),
 ("krabcice_krest_marie_kulichova_1906", "NAD-856/dao/images/0644/8ba90ed2-1c14-46fc-9b23-bf7581d780a5.jpg", (0.03,0.36,0.98,0.58)),
 ("krabcice_krest_antonin_kulich_1896", "NAD-856/dao/images/0644/28714468-690f-4649-a0a8-4e263e1f9365.jpg", (0.03,0.33,0.98,0.52)),
 ("krabcice_krest_emilie_kulichova_1900", "NAD-856/dao/images/0644/cc24645e-86b7-42fb-b02b-84ceab79f1ac.jpg", (0.03,0.10,0.98,0.32)),
]
for key, path, (a, b, c, d) in J:
    z.BASE = IMG
    full = f"zdroje/{key}.jpg"
    sys.argv = ["soal_zoomify.py", path, "1", full]
    z.main()
    w, h = map(int, subprocess.check_output(["magick", "identify", "-format", "%w %h", full]).split())
    subprocess.run(["magick", full, "-crop", f"{int((c-a)*w)}x{int((d-b)*h)}+{int(a*w)}+{int(b*h)}", "+repage",
                    "-resize", "1800x>", "-quality", "85", f"vyrezy/{key}.jpg"], check=True)
    print("ok", key)
