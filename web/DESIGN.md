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
