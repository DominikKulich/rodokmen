# Stav rodokmenu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Claude čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## Pro koho
- Výchozí osoba: Dominik Kulich, * 1995 Litoměřice
- Kdo s Claudem pracuje a jak chce komunikovat: Dominik sám; česky, stručně, technicky přesně.

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/osoby.py` | Přímí předci podle Kekulého čísla + rody, boční příbuzní, otevřené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (klíč = název obrázku). |
| `data/svazky.json` | Matriční svazky (archiv, signatura, odkaz). |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/udaje_od_rodiny.md` | Co řekla rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Rodinné dokumenty a fotky od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Rodinný web. `cd web && npm run data && npm run build`, náhled `npm run preview`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `osoby.py`, `zaznamy.json` a `research_log.md` (jméno, místo, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Čtení od pomocníků ověřím sám.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python3 -I tools/kontrola.py`.

## Rozpracováno (aktualizovat průběžně)
- Polákovi (Čunín u Konice, MZA Brno – Acta Publica, nástroj tools/mza_dz.py): doloženo František (1905) → Jan (1865) → Jan (asi 1838) → Martin (Křemenec). Bavlnkovi/Burešovi ze Stínavy (fara Ptení). Vazba Miloslav (1932) → František (1905): Dominikem 22. 10. 2026 definitivně potvrzený rodinný údaj.
- Polákovi – další kroky: křest Jana st. (asi 1838, Křemenec – fara Konice), 1. manželka Jana (1865) – zemřelí Konice 1888–1892; Krejčí z Konice (Filomena); Pospíšilovi.
- Kulichovi (Ledčice, SOA Litoměřice): v rejstříku oddaných L16/43 (1873–1918) žádný Kulich; L16/47, 48, 51 nedigitalizované. Potřeba rodný list dědy Václava (* asi 1936) z matričního úřadu.
- Kaštánkovi: křest Václava (1914) NALEZEN (Zvole kn. 16569, sn. 215). Sňatek Ignáce K. × Josefy Vykutilové 4. 5. 1903 NALEZEN (Bystřice kn. 15461, sn. 34). Křest Ignáce 1878 NALEZEN (kn. 15440, sn. 114). Sourozenci Václava (5) nalezeni v N Dolní Rožínka 1904–1924; Bystřice město 1902–1904 prohledáno – nic (nejstarší dítě Božena 1905). Dál: křest Josefy Vykutilové 25. 12. 1880 (Bystřice město, N kn. 15420, 1865–1887 – asi sn. 150–160); úmrtí Josefy před 1923; sňatek Ignáce st. × Františky Hradešínské (před 1878, O Bystřice kn. 15460, Domanín sn. 148–184) → příjmení Terezie, manželky Karla K.; pak sňatek Ignáce st. × Františky Hradešínské (O Bystřice kn. 15460, 1854–1894, oddíl Domanín sn. 148–184) a Vykutil × Kroutilová (tamtéž, oddíl Bystřice sn. 1–133); oddaní Zvole 1881–1949 (kn. 16571, Dolní Rožínka sn. 94–119) – sňatek Václava a Heleny 1941 (údaje o Heleně, její rodiče). Pozdější bydliště „Bratrušín“ – upřesnit (Bratrušov u Šumperka?).
- Šlosárovi: Helena * 20. 10. 1920 Malý Lapáš (okres Nitra, SK; farnost zjistit) → slovenské matriky 1920 (Štátny archív Nitra; FamilySearch „Slovakia Church and Synagogue Books“ obvykle končí kolem 1910, tak hledat rodiče a sňatek rodičů).
- Rodné listy dědů Václava a Miloslava: viz archivni_dotazy.md.


## Vizuál a oponentura (22. 10. 2026)
- Aktuální zadání vzhledu a pravidla časových údajů ve stromu jsou v `web/DESIGN.md` (sekce Požadavky uživatele a změny).
- Na úvodu je strom místo mapy. Oponentura je v `OPONENTURA.md`; Dominik již definitivně potvrdil návaznost Miloslava na Františka *1905; u legionáře nyní hledáme podrobnosti osobní vojenské služby.
- Nejistotu vazby eviduje `parent_link="prob"` nezávisle na doložení osoby. Data neměnit na jistá jen kvůli vzhledu.
- Krejčí: Filomena Krejčí – zjistit rok narození (křestní list Františky 1906, fara Olomouc–Nová Ulice, nebo sňatek/úmrtí Filomeny v Konici). Pak křest v N Konice (9079–9083) přes index kn. 9137.

## Pravidlo (Dominik, 22. 10. 2026)
Každý nalezený matriční zápis – i u sourozenců a bočních příbuzných – uložit jako plný zápis (zaznamy.json + výřez ve vyrezy/, snímek ve zdroje/, přepis v prepisy.json, rámeček v zvyrazneni.json) a připojit ke kartě osoby (r=[…] u předka i u SIDE). Web je na to ukazuje.
- Polákové: doloženo až po sňatek 1779 (Josef P. × Anna Popelková, Křemenec 7) a jeho otce Josefa P. Dál: křest Josefa ml. (~1750–1758) v N Konice 1750–1770 (kn. 9069, detail 5695) a starší (kn. 9068, 1680–1750). Dál: křest Jiřího Poláka (~1786) a Marianny Paulíkové (~1790) v N Konice 1786–1804 (kn. 9071, detail 5697), sňatek Josef Polák × ? (O Konice před 1786); Tilšerovi – křest Marianny (~1812, Veselá) v kn. 9072; Pospíšilovi – zjistit farnost Bílska.

## Sestavení webu (22. 10. 2026)
Před každým `astro build` spustit export dat (`npm run data` = `tools/export_web.py`), jinak web ukazuje starý `site.json`. Hotový web se kopíruje do `web/dist` i do `../web_rodokmen` (relativní odkazy).
- Polákové Čunín: děti Jana P. (*1838) kompletně 1860–1885 (7 dětí, doloženo). Otevřené: totožnost padlého Jana 1893–1915 – rejstřík O Konice 1893–1943 (kn. 9105) má jen sňatek Jana Poláka z Veselé 1917 (* 1890, syn Antonína – nesouvisí); Eduardův Jan (*16. 4. 1893) se v Konici do 1943 neoženil, sňatek vdovy Heleny Kmentové v Přemyslovicích 1916–1925 nenalezen. Dál: Z Konice 9125 (dodatečné zápisy 1919–1925), úmrtí Heleny, děti Eduarda.

## Rodinná šestadvacítka (23. 10. 2026)
Čunín čp. 26 u Františka Poláka (křest 1905, sňatek 1929) a Dolní Rožínka čp. 26 u Václava Kaštánka (křest 1914) znovu přečteny v obrazech. Dominik doplnil současné bydliště s maminkou Janou: Chudoslavice čp. 26, a výslovně požádal o zveřejnění v zajímavosti. Rozlišovat matriční doklady a současný rodinný údaj; datum sdělení není nastěhováním. Úvod aktualizován o Kaštánkovy i Šlosárovy.

## Sčítání Krejčích (23. 10. 2026)
Na výslovnou žádost Dominika přidány na web oba dodané výřezy sčítání Konice 1910 a 1921 s přepisy a vyznačením Františky. Vazba na Filomenu je silně podpořená, čtení zkratky Fil. předběžné; data prarodičů rozporná, číslo domu a archivní signaturu ověřit. Nové jisté osoby z těchto výřezů nevytvářeny.

## Miloslav a Třebařov (23. 10. 2026)
Dominik doplnil bydliště Miloslava s rodiči Františkem (*1905) a Františkou Krejčí (*1906) v Třebařově, bez roku přesunu a čísla domu. Přidán bratr Zdeněk Polák (SIDE u č. 6), životní data neznámá, a kolorovaná rodinná fotografie Miloslava pro kartu a strom. Vše nové evidováno jako rodinné sdělení.
