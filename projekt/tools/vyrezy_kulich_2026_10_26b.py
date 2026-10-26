#!/usr/bin/env python3
"""Výřezy zápisů Kulichů z Ledčic (L16/32 N 1868–1899, L16/43 O 1872–1922), nalezeno 26. 10. 2026.
Spustit z kořene projektu:  python3 tools/vyrezy_kulich_2026_10_26b.py"""
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
import soal_zoomify as z
IMG = "https://images.soalitomerice.cz/ximage/matriky/zoomify/cz/archives/CZ-214000010/"
J = [
 ("ledcice_krest_vaclav_kulich_1877", "NAD-856/dao/images/0500/10c21016-0398-48ac-b34f-958d96e8b460.jpg", (0.02,0.485,0.97,0.645)),
 ("ledcice_krest_julie_koubova_1878", "NAD-856/dao/images/0500/b8e49829-3ad3-44e5-8439-55f64e9c6cd2.jpg", (0.02,0.475,0.97,0.57)),
 ("ledcice_oddavky_vaclav_kulich_julie_koubova_1900", "NAD-856/dao/images/0501/ed13a0ba-ec2f-4684-8d65-97dc5463289d.jpg", (0.03,0.44,0.97,0.63)),
 ("ledcice_krest_josef_kulich_1870", "NAD-856/dao/images/0500/b7f7ac31-a04c-4e90-9860-d3aa25562ecf.jpg", (0.02,0.22,0.97,0.38)),
 ("ledcice_krest_rosalie_kulichova_1883", "NAD-856/dao/images/0500/e0797a12-e692-42a8-95f1-2a354f51cc3b.jpg", (0.02,0.68,0.97,0.86)),
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
