# Rodokmen – návrhy na vylepšení (22. 10. 2026)

## A. Hledání v archivech (největší úspora času)
1. **Jednotný přístup „najdi knihu → stáhni snímky“** – dnes má každý archiv vlastní skript (aron, trebon, soal, mza_dz, nacr).
   Společný modul `tools/archiv.py` s jedním rozhraním: `archiv.py <portal> knihy <obec>` a `archiv.py <portal> snimek <kniha> <n>`.
   Zoomify kód je dnes 2× (soal_zoomify + nacr) – sloučit.
2. **Náhledová mozaika knihy** jedním příkazem (`archiv.py … nahledy <kniha> 1-200 krok 5`) – dnes se dělá ručně přes montage;
   s ní najdu oddíl obce a rok během minuty.
3. **Mapa „obec → farnost → archiv“** v datech (`data/farnosti.json`): Čunín→Konice (MZA), Stínava→Ptení (MZA), Ledčice→L16 (SOA LT).
   Dnes se to dohledává pokaždé znovu.
4. **Pomocník pro rejstříky** – stáhnout jen písmeno z indexu (rejstříky mají na okraji záložky A–Z) a ukázat ho ke čtení.
5. **Fronta úkolů** `data/fronta.md` generovaná z osob: u každého předka „nejmladší chybějící událost + kniha + snímky“.
   Generovat skriptem (rozšíření `kontrola.py`).
6. **Databáze válek** – hotovo: `tools/valky.py` (1. a 2. sv. válka, holocaust). Kramerius ztrátové seznamy fungují po povolení
   domény `kramerius5.nkp.cz`; ostatní databáze jen přes prohlížeč (holocaust.cz, Yad Vashem, Arolsen, VÚA, Volksbund).
7. **Sčítání lidu 1869–1921** (SOA, AHMP) a **gruntovní knihy** – pro „mezeru“ 1915–1950 u Kulichů, kde chybí matriky.

## B. Kontrola Python skriptů
- Všechny skripty jdou přeložit (py_compile OK), chyby syntaxe nejsou.
- **ImageMagick 7 natvrdo** (`magick`) v 10 skriptech – přidat fallback: `shutil.which('magick') or 'convert'` (u montage/identify),
  nebo slepování dlaždic přes Pillow → bez závislosti na ImageMagick (jednodušší instalace na Windows).
- **Úklid dočasných souborů** – soal_zoomify/mza_dz nechávají `tmp…` a `.tmp.jpg`, když nejde mazat; psát do `pracovni/_tmp` a
  mazat best-effort (nacr.py už to dělá).
- **Sjednotit User-Agent, timeouty a opakování** (anno_snap, kramerius, soal bez UA) – jedna funkce `http.get()` s 3 pokusy.
- **mista.py** padá celý při jedné nedostupné obci → zachytit chybu a pokračovat; povolit ruční souřadnice z CLI.
- **kramerius.py** používá API v5 (kramerius5.nkp.cz) – NK přechází na Kramerius 7; přidat v7 jako záložní.
- **mza_dz.py** – urllib dostává 426 → curl; přepsat na `http.client` s HTTP/2 není v stdlib, curl je OK, jen hlídat jeho přítomnost.
- **export_web.py** – web.json bez přihlašovací odpovědi jen varuje; pro `npm run nasadit` by měl export skončit chybou.
- **Testy**: malá sada `tools/test_*.py` s ukázkovými daty (ukázka Novákových) – kontrola exportu a kontroly dat po změnách.

## C. Web – nové funkce
1. **Hledání offline** – Pagefind v lokální verzi nejede; přidat jednoduché vyhledávání v JSON (jména, obce, roky) přímo v JS.
2. **Rodokmen jako strom** (vedle vějíře) – klasický „pedigree“ zleva doprava, klikací, s fotkami.
3. **Statistiky rodu** – dožití, věk při sňatku, povolání v čase, počet dětí; graf podle generací.
4. **Časová osa** – přepínač „jen přímí předci / i sourozenci“, filtr podle obce, mini-mapa u událostí.
5. **Stránka obce** – všichni předci z obce, čísla domů, odkaz na matriky, historie obce (Wikipedie odkaz).
6. **Dům a čísla popisná** – „rod sto let v jednom domě“ (Čunín čp. 26) jako zajímavost automaticky.
7. **Porovnání zápisů** – u osoby vedle sebe křest/sňatek/úmrtí s výřezy a rozdíly (datum 9. vs 16. 2. 1892).
8. **Tisk / PDF** – rodový list jedné osoby nebo celé větve na A4; vějíř jako plakát už je (`fan_chart.py`).
9. **Dějinný kontext k obcím** – války, morové roky, cholera 1866, kolektivizace – na časové ose už je, rozšířit o regionální.
10. **Stará mapa** – hotovo; doplnit hranici Čech a Moravy a historické názvy obcí (Fröhlichsdorf = Veselá).
11. **Sdílení s rodinou** – Netlify s přihlašovací otázkou; „Co hledáme“ s formulářem, kam příbuzní napíšou, co vědí.

## D. Data a metodika
- **Zdroj ke každému faktu** (dnes jen k osobě) – u faktu odkaz na zápis, ze kterého je.
- **Stav „doc“ jen přímo čtené** – dnes je celá větev doc i u jmen čtených nepřímo; rozlišit „doc (vlastní zápis)“ a „doc (z cizího zápisu)“.
- **Boční příbuzní z matrik** (bratři Jana Poláka) systematicky – pomáhají ověřit rodinu a najdou živé vzdálené příbuzné.
- **Rodné listy dědů** (Václav Kulich, Miloslav Polák) z matrik – uzavřou dvě nejslabší místa stromu.

## Hotovo (22. 10. 2026)
- Web: motiv „Strom“ (viz `projekt/web/DESIGN.md`), ilustrovaný strom předků, statistiky, stránky obcí s domy (čp.),
  offline hledání, filtr obcí na časové ose, tisk do PDF (rodový list, strom A3, rodová kniha `/kniha/`),
  porovnání zápisů u osoby, formulář pro příbuzné, stará mapa s hranicí Čech a Moravy a německými názvy obcí.
- `valky.py --kramerius`: čte text ztrátových seznamů, vyřízne zápisy a řadí je podle shody s rokem narození a obcí.
- Zbývá: B (sjednocení archivních skriptů, ImageMagick fallback, testy), A1–A5, D.
