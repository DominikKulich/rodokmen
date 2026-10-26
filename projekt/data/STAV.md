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
- Kulichovi (Ledčice, SOA Litoměřice): L16/47 je už digitalizovaná – sňatek pradědy Václava Kulicha (* 2. 11. 1900) a Anny Tiché (* 9. 10. 1899) 15. 2. 1925 Černouček (sn. 67). Další kroky: křest Anny Tiché (N Ledčice 1868–1899, tom. VI fol. 157), křest Václava 1900 (tom. 1900 fol. 7 – zjistit, zda je digitalizován), sňatek a původ Václava st. × Julie Koubové (v rejstříku L16/43 1873–1918 Kulich nebyl – ověřit znovu, případně jiná farnost), vztah k Janu Kulichovi z Ledčic čp. 82 (otec Františka Kulicha z Vražkova). Výřezy staženy 26. 10. 2026 (tools/vyrezy_kulich_2026_10_26.py). Rodný list dědy (* asi 1936) z matričního úřadu stále užitečný. Úmrtí Anny Tiché (rodinné vyprávění o dvou Annách) online ověřit nejde – úmrtní matriky Ledčic po r. 1867 nejsou digitalizované (L16/46 je jen Horní Beřkovice, bez Kulichů); rozhodne rodný list dědy (jméno matky) nebo dotaz na SOA/matriční úřad.
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

## Americká stopa Vykutilových (23. 10. 2026)
Cousin Finder navrhuje vztah přes Macek Family Tree: Marie Prochaska (1881–1916), bratr Frank Vykutil bez narození, bydliště, partnerky a dětí, rodiče skrytí. Ztotožnění Franka s naším Františkem není doložené; nepřipojovat jako jistou rodinnou větev. Na Dominikovu žádost zveřejněno v zajímavostech jako neověřená americká stopa, bez jmen žijících členů cizí rodiny.

## Audit přírůstků MyHeritage (23. 10. 2026)
Porovnán celý dodaný export 133 osob / 44 rodin s původními 84 osobami. Přibylo 49 záznamů, z toho 2 bezejmenné. Soupis a výsledky jsou v `AUDIT_MYHERITAGE_2026-10-23.md`, veřejný přehled na `/novinky/`, datově `myheritage_audit.json`. Nové cizí větve NEJSOU ověřeny: MZA přestal odpovídat. Přednost má křest Josefy Vykutilové 25. 12. 1880 v Olešné (N 15997; index 16005), aby se prokázala návaznost na Františka *1843. U Marie *1870 v exportu nesprávně Kroutilová; dodaný výřez matky Hrnčířovy a otcovských prarodičů uložen jako samostatný, dosud rodině nepřiřazený pramen. Pět čunínských křtů má znovu přečtené čp. 25, ne 26 z exportu. Hlavní strom neprodloužen podle nepotvrzených shod. Fotografie Václava a původní Heleny přeneseny; 1942 Jana Helena a Miloslav *1960 jako rodinné údaje. Do účtu MyHeritage při auditu nezasahováno.

### Novější pokyn Dominika: převzaté větve zobrazovat i ve stromu
Sedm nových přímých předků má st=mh a parent_link=prob: 117, 202, 203, 224, 225, 234, 235. Jsou vidět ve stromu; rodičovství a přesná data zatím neověřeny. Nepovažovat předchozí větu „hlavní strom neprodloužen“ za aktuální pokyn.

## Nalezen křest Františky Krejčí 1906 (23. 10. 2026)
ZA Opava, porodnice Nová Ulice, O IX 13, inv. 11285, sn. 178 / fol. 177 / č. 197. N 10. 11., křest 12. 11. 1906; Filomena 18 let, dcera Františka Krejčího a Františky, Konice. Doplněni předci 54 a 55, Filomena doc a narození pouze odhad asi 1887–1888. Kmotra Marie Wěrník (?) – ověřit přesné příjmení, vdova opakovaná u jiných dětí porodnice, nikoli doložená příbuzná. Křemenec nové rodinné sdělení. Dál vlastní křest Filomeny 1887–1888, sňatek jejích rodičů a pobyt v Křemenci; MZA vyžaduje HTTP/2 (pracovni/krejci_mza_http2.mjs). Rejstřík 9137 detail 5749 sn. 37 pokrývá K 1886–1890, sn. 36 předchozí roky; čtení bledých jmen u vazby nejisté.

### Upřesnění rodinné stopy ke Křemenci
Dominik 23. 10. 2026 upřesnil: v Křemenci bydlela kmotra Františky Krejčí. Jméno ani čp. neuvedeno. Totožnost této kmotry s Marií Wěrník (?) z porodního zápisu 1906 není prokázána. Pobyt Františky ani Filomeny v Křemenci tím nedokládat.

## Sčítání Polákových 1900 – Čunín 92
Dominik dodal celý arch, archivní signatura dosud neznámá. Osoby 48/49 doplněny o pramen cunin_scitani_jan_polak_1900. Jan tkalcovství, vedlejší polní hospodářství; gramotnost Jan čte/píše, Anna jen čte. Nový údaj o Anně 26. 6. 1835 Bílsko je ze sčítání, nikoli křest. Dál N Anny a N Josefa Poláka 26. 4. 1887 Křemenec, tovaryš u Jana v roce 1900, příbuznost neprokázána. Nepřidávat Josefa jako syna/vnuka bez křtu. Dům 92 neruší jiné starší adresy rodiny. Zpráva POLAK_SCITANI_1900_2026-10-23.md.

### 23. 10. 2026 – úplný přenos exportu a sčítání
Dodaný MyHeritage export: 133 osob, 44 rodin, 202 veřejných událostí; všechno v data/myheritage_import.json a na /myheritage/. Zvlášť doplněna úmrtí Františky Bavlnkové 1947, Františka Poláka 1983 a Františky Krejčí 1984 do karet i roků stromu. Jde o data exportu, nikoli automaticky ověřené matriky. Sčítání Čunín 13 nově zpracováno (legionář); Čunín 92 společný doklad Jana a Anny bez duplicit. Anna: polský původ nedoložen; její vlastní křest a úmrtní doklad zůstávají otevřené. Další změny živého MyHeritage po tomto exportu nejsou součástí přenosu.

### 23. 10. 2026 – starší Polákovi, další přesná stopa
Pracovní hypotéza: Josef ženatý1779 může být kandidát N1748 Křemenec, rodiče Josef+Kateřina (9068 401/798). Možný sňatek rodičů1733 Josef, syn Jana, a Kateřina Křupková, dcera Jiřího z Přemyslovic (9097 35/68). Kandidát otce1708 Jan+Anna (9068 175/347). Neověřeno originály, do hlavního stromu nepřidáno. MZA opakovaně timeoutoval; neznamená konec matrik. První další krok přečíst 9068 401 a 9097 35 a vyřešit Z1772/1775 (mohou být děti Josefa+Růženy). Úplný rozbor POLAK_STARSÍ_2026-10-23.md; HTML indexů v pracovni/polak-starsi-20261023/.

### 26. 10. 2026 – vojenské karty Kulichů, přepis
Dodáno8screenshotů západního vojska; 7unikátních obrazů (7/8duplicita). Přepisy a původní přílohy v dokumenty/kulich-zapad-1940-1945-2026-10-26/; PREHLED.html ukazuje snímky vedle textu, PREPISY_KULICH_ZAPAD_2026-10-26.md celý přepis. Neprokázané přiřazení rubů narození20.4.1902a30.1.1902 k dvěma Janovým lícůmH849/C1515, nutno přes původní archivní odkazy. Bohumil1902 s RAF, František1907 demobilizace1945, Josef1908 zajetí1940–1945. Žádné nové prokázané příbuzenství, hlavní strom ani veřejný web tímto přepisem neměněn.

### 26. 10. 2026 – Kulichové z Ledčic
Praděda Václav Kulich (* 2. 11. 1900 Ledčice 85) × 15. 2. 1925 Černouček Anna Tichá (* 9. 10. 1899 Ledčice 23) – L16/47 s. 62. Pra-prarodiče Václav Kulich († před 1925, domkář a tesař, Ledčice 85) + Julie Koubová (Ledčice 94); Josef Tichý (dělník, Ledčice 23) + Anna Kohlová (?). Evangelická linie z Vražkova čp. 71 (František Kulich, syn Jana Kulicha z Ledčic 82; děti Antonín 1896, Emilie 1900, Marie 1906) zatím jen jako pravděpodobně příbuzná – v zaznamy.json bez napojení na osoby. Prohledáno bez výsledku: N39/20 sňatky 1926–1936, N39/19 narození 1895–1909 (Václav), C21/A civilní sňatky 1927–1933.

### 26. 10. 2026 – sčítání Kulichů 1921
Otcova větev přes Luboše (upřesnil Dominik). Ledčice85: Anna Kulichová1854 vdova a pět vnoučat včetně Václava2.11.1900. Jaroslav4.6.1908, Jan13.4.1910, Anna22.9.1911, Marie22.8.1914. Vnoučata neoznačovat automaticky za sourozence. Babička bez potvrzeného rodného příjmení a strany příbuzenství, zapsána u vedlejších příbuzných. Dál sčítání1910/1900 a narození dětí.
