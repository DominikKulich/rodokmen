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
