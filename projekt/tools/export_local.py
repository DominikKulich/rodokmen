"""Z již sestaveného web/dist aktualizuje dvojklikem otevíratelný web_rodokmen.
Spustit po export_web.py a sestavení Astro. Původní HTML kopie se zálohuje.
"""
from pathlib import Path
from datetime import datetime
import os
import re
import shutil
import tempfile
import time
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'web' / 'dist'
DEST = ROOT.parent / 'web_rodokmen'


def write_text_safely(target, text):
    """Nahradí celý soubor, aby export netrunkoval soubor právě synchronizovaný OneDrivem."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=target.parent,
                                         prefix='.export-', suffix='.tmp', delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(text)
        for attempt in range(5):
            try:
                os.replace(temporary, target)
                return
            except OSError as error:
                # OneDrive může krátce vracet EACCES, EINVAL nebo chybu sdílení.
                if attempt == 4 or (error.errno not in (13, 22) and getattr(error, 'winerror', None) not in (5, 32, 33)):
                    raise
                time.sleep(0.2 * (attempt + 1))
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def main():
    if not (SOURCE / 'index.html').is_file():
        raise SystemExit('Nejprve sestavte web do projekt/web/dist.')
    if DEST.exists():
        backup = ROOT / 'pracovni' / ('web_rodokmen-zaloha-' + datetime.now().strftime('%Y%m%d-%H%M%S'))
        backup.parent.mkdir(exist_ok=True)
        shutil.make_archive(str(backup), 'zip', DEST)
        print('Záloha:', str(backup) + '.zip')
    shutil.copytree(SOURCE, DEST, dirs_exist_ok=True)
    shutil.copy2(ROOT / 'web' / 'DESIGN.md', DEST / 'DESIGN.md')
    if (ROOT / 'OPONENTURA.md').exists():
        shutil.copy2(ROOT / 'OPONENTURA.md', DEST / 'OPONENTURA.md')
    for report in ROOT.glob('VALKY_*.md'):
        shutil.copy2(report, DEST / report.name)
    count = 0
    # Zpracovat jen soubory aktuálního sestavení; staré vlastní soubory nemažeme.
    for source in SOURCE.rglob('*.html'):
        target = DEST / source.relative_to(SOURCE)
        text = source.read_text(encoding='utf-8')
        def replace(match):
            attr, quote, url = match.groups()
            parts = urlsplit(url)
            path = parts.path.lstrip('/')
            if not path or path.endswith('/'):
                path += 'index.html'
            relative = os.path.relpath(DEST / path, target.parent).replace('\\', '/')
            if parts.query:
                relative += '?' + parts.query
            if parts.fragment:
                relative += '#' + parts.fragment
            return attr + '=' + quote + relative + quote
        # Pouze skutečné značky HTML; řetězce v inline skriptech zůstávají beze změny.
        chunks = re.split(r'(<script\b[^>]*>.*?</script>)', text, flags=re.S | re.I)
        for i in range(0, len(chunks), 2):
            chunks[i] = re.sub(r'''\b(href|src|action)=(["'])(/(?!/)[^"']*)\2''', replace, chunks[i])
        write_text_safely(target, ''.join(chunks))
        count += 1
    (DEST / 'CTI_ME.txt').write_text(
        'Rodokmen Kulichových – lokální kopie webu\n'
        'Otevři index.html dvojklikem. Odkazy jsou relativní.\n'
        'Zdrojové soubory: ../projekt/web/src\n'
        'Po sestavení webu aktualizace: python projekt/tools/export_local.py\n'
        'Web není chráněn heslem; jde o místní kopii.\n', encoding='utf-8')
    print(f'Aktualizováno {count} HTML stránek: {DEST}')


if __name__ == '__main__':
    main()
