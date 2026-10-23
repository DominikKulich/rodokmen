# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


- soal_zoomify.py: BASE končí „…/CZ-214000010/matriky/“, ale aktuální cesty obrázků jsou „…/CZ-214000010/NAD-856/dao/images/0501/<uuid>.jpg“ (bez „matriky/“). Cesta se liší snímek od snímku (uuid), proto: v prohlížeči z <select class="getScanSelect"> vzít id snímků a pro každý fetch('/digitalnibadatelna/showZoomify/<id záznamu>/<id snímku>') → zoomifyImgPath. 1 dotaz na snímek.
- Ověření přístupu (PoW) v digi.soalitomerice.cz stojí, když je panel prohlížeče skrytý (throttling na pozadí) – uživatel musí panel zobrazit.
- Windows/Linux VM bez ImageMagick 7: stačí shim `magick` → convert/identify/montage (IM6).
- Síť: archivní domény nejsou ve výchozím allowlistu – uživatel je musí přidat v Nastavení → Capabilities.
- Starý GenoPro .gno (OLE soubor, stream Contents, XOR 0x08): jména a povolání čitelná, data binárně (neznámý formát).

- Acta Publica (MZA Brno): snímky bez přihlášení. Nový nástroj tools/mza_dz.py (Deepzoom dlaždice z /iipsrv/iipsrv.fcgi?Deepzoom=/srv/LUNxxx/…/<kniha>-NNNNN.jp2.dzi). CVT=jpeg vrací 403, Deepzoom chce Referer, urllib dostane 426 → curl; plné rozlišení ~500 dlaždic → paralelně. LUN složka se liší podle knihy (LUN105, LUN106…) – vzít z network requestu v prohlížeči. Číslování souborů: některé knihy začínají -00000, jiné -00010.
- Konice kn. 9106: oddací kniha s oddíly po obcích, hlavička „Str.“ = strana z rejstříku (sn. ≈ str. + 2 pro Konici, sn. ≈ str. − 5 pro Čunín).
- Past: v rejstříku psaném zkratkovitě se snadno splete Polák/Pavlík – ověřit na stránce zápisu.
# 23. 10. 2026 – export do složky synchronizované OneDrivem

Přímé přepsání HTML krátce po kopírování může ve Windows vracet přechodné OSError EINVAL/EACCES. Osvědčil se zápis do dočasného souboru ve stejné složce a atomické nahrazení přes os.replace s omezeným opakováním při chybě sdílení; potom kontrola všech místních odkazů a obrázků. Samotné opakované spuštění celého exportu nebylo spolehlivé.

