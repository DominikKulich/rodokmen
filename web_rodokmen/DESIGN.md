# Vzhled webu – motiv „Strom“

Celý web vychází z ilustrovaného stromu předků (`/strom/`, komponenta `src/components/StromIlustrace.astro`).
Inspirací byl obraz rodokmenu z filmu (zelené dřevo, zlaté listí, jména na stuhách). Je to **vlastní návrh**:
nepřebíráme erb, havrany, motto ani portréty z filmového obrazu.

Styly: `src/styles/global.css` (rozvržení, komponenty) + `src/styles/theme.css` (barvy, materiály, tisk) – theme se načítá po global
a přepisuje jen barvy a povrchy. Barvy měnit **jen přes proměnné v `theme.css`**.

## Paleta

| Proměnná | Barva | Použití |
|---|---|---|
| `--wood` | `#1f3a28` | podklad stránky (zelené dřevo s kresbou), nadpisy, tmavá tlačítka |
| `--wood-dark` | `#142619` | hlavička |
| `--wood-light` | `#2c4d33` | hover tlačítek, kresba dřeva |
| `--gold` | `#c9a13a` | linky, rámečky, ornament ❦ u nadpisů, rám listu |
| `--gold-light` | `#e7c96c` | text na dřevě (název webu, iniciály, text tlačítek) |
| `--parch` | `#efe6cb` | pergamen – list s obsahem (`main`) |
| `--paper` | `#f8f2df` | karty, zápisy, tabulky (světlejší pergamen) |
| `--ink` | `#2e2416` | text |
| `--muted` | `#6a5536` | vedlejší text |
| `--line` | `#cdbb8f` | okraje karet |
| `--wax` / `--accent` | `#8e2b22` | odkazy, pečeť „doloženo“ |
| `--bark` | `#3b2b1c` | větve, kmen |
| `--leaf` | `#86a043` | zelené listy |
| `--rose` | `#e3c2bb` | květy a poupata |
| `--doc` / `--prob` | `#3f6b2f` / `#8a5a12` | stav: doloženo / pravděpodobné |

Listí stromu míchá zlaté a olivové odstíny: `#d8b44c #caa23c #e7c96c #a9b553 #86a043 #bfa046`.
Barvy rodů (kroužky ve stromu, tečky na mapě) jsou v `data/osoby.py` (LINES) a zůstávají.

## Písmo
- Nadpisy a název webu: serif (Georgia), **h1 kurzívou**, název v hlavičce zlatou kurzívou.
- Text: systémové bezpatkové písmo.
- Ve stromu: jména kapitálkami (small-caps), pravděpodobné osoby kurzívou.

## Materiály a prvky
- **Podklad**: sametově zelený radiální přechod (světlo nahoře uprostřed `#36663f` → okraje `#0d1d12`) + zlatý ornament
  „damašek“ z listů (vlastní motiv, dlaždice 160 px, průhlednost 7,5 %), obojí `background-attachment: fixed`.
  Dlaždici generuje skript popsaný v historii gitu; ve stromu je stejný motiv jako `<pattern id="damask">`.
- **List s obsahem**: pergamenový přechod, dvojitý vnitřní rámeček (hnědá linka + zlatá linka 7 px od okraje), stín.
- **Nadpis h2**: zlatá linka pod nadpisem a lísteček ❦ před ním.
- **Tlačítko `.btn`**: zelené dřevo, zlatý text a rámeček; `.btn-light` = pergamen.
- **Strom**: pozadí = stejný přechod a damašek + měkká zlatá záře za korunou; v rozích zlaté rozviliny s lístky
  (vlastní ornament, `#roh`); stuhy (pergamen s přeloženými konci), medailon s iniciálami a kroužkem v barvě rodu,
  červená pečeť ✓ = doloženo matrikou, poupě = neznámý předek (odkaz na „Co hledáme“).

## Tisk / PDF
- `@media print` v `theme.css`: bílé pozadí, bez menu a filtrů, karty se nedělí přes stránky, otevřou se přepisy (`details`).
- Třídy: `.no-print` (skrýt v tisku), `.print-only` (jen v tisku), `.page-break` (nová strana).
- Strom se tiskne na **A3 na šířku** (pojmenovaná stránka `@page strom`, obal `.strom-print`).
- `/kniha/` = rodová kniha pro tisk do PDF: obálka se stromem, obsah, kapitola na generaci, u osob fakta, rodiče a zápisy s výřezy.
- Karta osoby má tlačítko „Rodový list / PDF“.
- V dialogu tisku zapnout „Grafika na pozadí“, jinak zmizí barvy.

## Zásady
- Na zeleném podkladu jen zlatý nebo krémový text; tmavý text jen na pergamenu.
- Nové stránky: obsah do `<Base>`, karty `.card`, nadpisy h2 – motiv se aplikuje sám.
- Mobil: list s obsahem bez okrajů (od 640 px dolů), strom se posouvá vodorovně.


## Požadavky uživatele a změny — 22. října 2026

- Celkový směr: rodová tapisérie inspirovaná rodokmenem Blackových z Harryho Pottera. Tmavá sametově zelená, patinované zlato, pergamen, jemné rostlinné větvení a historická patková typografie. Jména musí zůstat skutečným textem a odkazy.
- Hlavní stránka má přímo zobrazovat interaktivní strom namísto mapy. Mapa zůstává na /mapa/. Vějíř zůstává na /vejir/, ne jako druhý velký strom na úvodu.
- Stejná komponenta StromIlustrace.astro patří na úvod i /strom/. Zachovat přiblížení, posouvání, odkazy na osoby a tisk.
- Pod jménem zobrazit dostupné roky života či narození; přibližné narození musí mít značku ≈. Opraven export, který u „* asi 1838“ ztrácel přibližnost.
- Nemá-li osoba roky, zobrazit „zmínka 1862“ nebo „zmínka 1862–1870“ podle roků jejích citovaných zápisů. To je doložený časový kontext, nikoli tvrzení, že předek v době zápisu žil. Zápis vnuka může zmiňovat již zemřelého děda.
- Bez let a bez datovaných dokladů zobrazit „doba zatím neurčena“. Nevymýšlet roky narození odečítáním 25/30 let za generaci.
- Zlatý bod znamená doložení osoby, nikoli automaticky doložení celé linie. parent_link="prob" v data/osoby.py se exportuje jako parentLink a vykreslí přerušovanou větev; karta osoby vysvětluje nejistotu.
- Komponenta přiděluje jednotlivým větvím prostor podle potomků v zobrazení. Prázdné konce mají menší šířku. U nových dat znovu vizuálně ověřit dlouhá jména.
- Oponentura dat, skriptů a matrik: ../OPONENTURA.md. Aktuální sestavení: dist/; nadřazená složka web_rodokmen je hlavní předávaná lokální verze a musí se vždy aktualizovat.

## Předání lokálního webu
Uživatel otevírá `../../web_rodokmen/index.html` dvojklikem. Po každé změně exportovat data, sestavit web a spustit `python tools/export_local.py` z projektu. Nestačí aktualizovat pouze web/dist. Skript zálohuje původní kopii do pracovni a převádí odkazy na relativní.


## Rodová malba a ovládání — doplnění uživatele
Hotový web musí být kompletně ve web_rodokmen. Strom má připomínat krásnou rodovou malbu 19. století: zlacené lemy, rohové rozviliny, botanické listoví, kmen a kořeny, medailony. Roky mají být větší a kontrastní. Tažení myší posouvá plochu, krátký klik otevírá osobu; po skutečném tažení se proklik potlačí. Na dotyku ponechat přirozené posouvání. Zachovat tlačítka přiblížení a ovládání klávesnicí.

## Legionářská větev — 22. 10. 2026
Úvod nyní začíná oznámením „V naší rodině byl legionář“ a odkazuje na /legionar/. Stránka obsahuje doložené údaje Františka Poláka *1890, časovou osu, výřezy jeho narození a sňatku rodičů a odkazy na společné předky a ČsOL. Komponenta LegionarskaVetev.astro zobrazuje obě bratranecké větve až po společné prarodiče, včetně jejich rodičů. Je součástí stránky příběhu i komponenty hlavního stromu (úvod a /strom/), s vlastním přiblížením a tažením. Jde o výslovně popsanou vedlejší větev; nepřidělovat jí smyšlená Kekulého čísla přímých předků. Matriční podklady a nejistoty popisuje VALKY_2026-10-22.md; přesné narození rodičů ani přímá vazba na Miloslava *1932 zatím nejsou doloženy.

Na začátku /legionar/ je původní portrét z galerie ČsOL (83965.006) ve zlatém rámu. Zachovat celý snímek i značku poskytovatele; proklik otevírá místní originál. Popisek odkazuje na zdroj; neodhadovat rok pořízení ani vyznamenání. Provenience a druhá digitální kopie téhož portrétu jsou evidovány v data/fotografie_legionar.json.

Další upřesnění uživatele: legionář nyní patří přímo do SVG hlavního stromu, nikoli pouze do samostatného přehledu. Větev nalevo od Polákových ve stejné malbě je připojena ke společným předkům č. 48 a 49, obsahuje otce Františka, matku Marii Trnkovou, její rodiče Josefa Trnku a Annu a legionáře s pravým portrétem. Odkazy vedou na sňatek rodičů a příběh s dokumentací. Tlačítko „Legionář a rodiče“ větev vycentruje; samotný hlavní strom nepřiděluje vedlejším osobám čísla přímých předků. Samostatná komponenta LegionarskaVetev zůstává jen na stránce příběhu. Fotografie je také na hlavním úvodu místo dekorativního obrázku.

## Celý web a historický kontext
Legionářská karta je v zajímavostech, rodové knize, rodové stránce Poláků, Čuníně a u seznamu přímých předků (vysvětlena vedlejší příbuznost). Statistiky ho nezapočítávají do přímých předků. Časová osa z data/legionar.json přebírá pět doložených událostí a plukovní kontext drží odděleně jako dějinné mezníky. Příběh a kniha obsahují sekci Zborov a magistrála se zdroji VHÚ/MO a výslovnou mezí: osobní bojová účast je otevřená. Dominikovo definitivní potvrzení návaznosti Miloslava je v parent_link="fam", nikoli nový matriční doklad.

## Umístění legionářské větve
Na přání uživatele je legionářská větev nalevo od hlavní větve Poláků, mezi ní a otcovskou větví. Plocha se vkládá před podstrom č. 12; ostatní větve se posouvají, aby zůstaly medailony oddělené. Připojení ke společným předkům i tlačítko přiblížení používají nové souřadnice.

## Zjednodušení legionářské větve
Na další výslovné přání uživatele zobrazuje hlavní strom jen Františka Poláka (*asi1860), syna Jana Poláka a Anny Pospíšilové, a pod ním jeho syna legionáře Františka (*1890). Medailony Marie Trnkové, Josefa Trnky a Anny jsou z hlavní malby odstraněny; příběh legionáře, citace a genealogická data zůstávají úplné. Levý prostor je zúžen a přiblížení je označeno „Legionář a otec“.

Poslední upřesnění: oba Františkové jsou přímo pod Janem Polákem (*asi1838), na jeho souřadnici X, po jedné generaci dolů. Boční rámeček a vložená mezera byly odstraněny; větev je začleněná do hlavní malby. Anna Pospíšilová zůstává vysvětlená jako matka staršího Františka v legendě i pramenech.

## 23. 10. 2026 – prémiovější pozadí
Na přání Dominika hlubší lesní zelená s jemným zlatým rostlinným damaskem, světlý pergamen s jemným zrnem, mosazné linky a rohový ornament. Vektorové dekorace v src/assets; nepoužívají externí zdroje ani animace. Tisk zůstává bílý a mobil omezuje pevná pozadí. Přidány Novinky v menu a na úvodní stránku.
