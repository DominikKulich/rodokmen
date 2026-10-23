#!/usr/bin/env python3
"""Hledání předků v databázích obětí a vojáků 1. a 2. světové války.

Použití (z kořene projektu):
  valky.py "Příjmení" [Jméno] [--narozen ROK] [--obec Obec ...] [--kramerius] [--vystup soubor.md]
Vypíše připravené dotazy a odkazy do všech zdrojů a s --kramerius prohledá c. a k. ztrátové seznamy
(Verlustliste 1914–1919) v Krameriu NK ČR: stáhne text nalezených stran, vyřízne zápisy dané osoby
(jméno, pluk, země, okres, obec, rok narození, osud) a seřadí je podle shody s rokem narození a obcí.
Německé tvary jmen i obcí se doplní samy (Karel→Karl, Klatovy→Klattau); chybějící obec dej přes --obec-de.

Zdroje (domény přidej do allowlistu jen ty, které použiješ):
 1. sv. válka
  - VÚA – databáze VHA: padlí v 1. sv. válce, legionáři ........ www.vuapraha.cz (databaze-vha) – v prohlížeči
  - Ztrátové seznamy Verlustliste (Kramerius NK ČR) ............ kramerius5.nkp.cz – tímto skriptem (--kramerius)
  - Legie 100 / Legionářský archiv .............................. www.legie100.com – v prohlížeči
  - Evidence válečných hrobů (MO ČR), obě války ................. evidencevh.army.cz – v prohlížeči
  - Kriegsarchiv Wien – kmenové listy přes FamilySearch .......... familysearch.org (katalog: pluk německy)
 2. sv. válka a holocaust
  - Databáze obětí (Terezínská iniciativa) ...................... www.holocaust.cz/databaze-obeti – v prohlížeči
  - Yad Vashem – Central Database of Shoah Victims' Names ........ collections.yadvashem.org – v prohlížeči
  - Arolsen Archives (koncentrační tábory, nucené práce, DP) ...... collections.arolsen-archives.org – v prohlížeči
  - EHRI – oběti Terezína + archivní fondy ...................... portal.ehri-project.eu – v prohlížeči
  - VÚA – padlí ve 2. sv. válce, příslušníci zahr. armád ........ www.vuapraha.cz – v prohlížeči
  - Volksbund – Gräbersuche (padlí ve wehrmachtu, Sudety) ........ www.volksbund.de/erinnern-gedenken/graebersuche-online
  - Památník Terezín – databáze politicky a rasově pronásledovaných (Malá pevnost, gestapo) – www.pamatnik-terezin.cz
Výsledky jsou vodítko – ověř v matrice (úmrtí v Terezíně: ohledací listy NA, HBMa inv. 2956; padlí 1914–18 mají
záznam i v matrice zemřelých domovské farnosti, často s pozdějším zápisem).
"""
import argparse, difflib, json, re, time, unicodedata, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor


def bez_diakritiky(s):
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode()


NEM = {"Jan": "Johann", "Josef": "Josef", "Karel": "Karl", "František": "Franz", "Václav": "Wenzel", "Antonín": "Anton",
       "Jiří": "Georg", "Vojtěch": "Adalbert", "Matěj": "Mathias", "Jakub": "Jakob", "Tomáš": "Thomas", "Martin": "Martin",
       "Pavel": "Paul", "Petr": "Peter", "Emil": "Emil", "Adolf": "Adolf", "Ludvík": "Ludwig", "Eduard": "Eduard"}


def varianty(prijmeni, jmeno):
    p = {prijmeni, bez_diakritiky(prijmeni)}
    if prijmeni.endswith("ák"): p.add(bez_diakritiky(prijmeni)[:-2] + "ak")
    if "ol" in prijmeni.lower(): p.add(bez_diakritiky(prijmeni).replace("ol", "oll"))
    j = {jmeno, bez_diakritiky(jmeno), NEM.get(jmeno, jmeno)} if jmeno else {""}
    return sorted(p), sorted(x for x in j)


# Německé názvy obcí a okresů, jak je uvádějí ztrátové seznamy (doplňuj podle potřeby).
OBCE_DE = {   # jen ověřené názvy; české názvy vesnic ztrátové seznamy často píší česky bez háčků (Dolin, Chudonice)
    "Klatovy": "Klattau", "Litoměřice": "Leitmeritz", "Roudnice nad Labem": "Raudnitz", "Roudnice": "Raudnitz",
    "Mělník": "Melnik", "Slaný": "Schlan", "Konice": "Konitz", "Prostějov": "Prossnitz", "Olomouc": "Olmütz",
    "Veselá": "Fröhlichsdorf", "Moravská Třebová": "Mährisch-Trübau", "Litovel": "Littau", "Boskovice": "Boskowitz",
    "Praha": "Prag", "Brno": "Brünn", "Plzeň": "Pilsen", "Domažlice": "Taus", "Sušice": "Schüttenhofen",
    "Strakonice": "Strakonitz", "Poděbrady": "Podiebrad", "Nový Bydžov": "Neu-Bidschow",
}
STAV = [("krank", "nemocen"), ("k", "zajat"), ("verm", "nezvěstný"), ("verw", "raněn"), ("tot", "padl"), ("gest", "zemřel"),
        ("krank", "nemocen"), ("gefallen", "padl")]
STAV_RE = re.compile(r"\b(k\w{0,4}egs\s?gef\w*|verm\w*|ver[w«]\w*|tot|gest\w*|krank\w*|gefallen)\.?(\s*\([^)]{0,40}\))?", re.I)
API = "https://kramerius5.nkp.cz/search/api/v5.0/"


def _get(url, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": "rodokmen-skill (genealogie)"})
    for pokus in range(3):
        try:
            return urllib.request.urlopen(req, timeout=timeout).read()
        except Exception:
            if pokus == 2: raise
            time.sleep(2 * (pokus + 1))


def ocr(pid):
    """Text OCR stránky (Kramerius ho vrací v UTF-16 s BOM, starší objekty v UTF-8)."""
    b = _get(f"{API}item/{pid}/streams/TEXT_OCR")
    if b[:2] in (b"\xff\xfe", b"\xfe\xff"): t = b.decode("utf-16")
    else: t = b.decode("utf-8", "replace")
    t = re.sub(r"-\s*\r?\n\s*", "", t)          # rozdělená slova
    return re.sub(r"\s+", " ", t)


def podobne(a, b, prah=0.8):
    a, b = bez_diakritiky(a).lower(), bez_diakritiky(b).lower()
    return a == b or (len(a) > 3 and difflib.SequenceMatcher(None, a, b).ratio() >= prah)


def zaznamy(text, prijmeni):
    """Vyřízne z OCR stránky jednotlivé zápisy začínající příjmením (konec = údaj o osudu: tot/verw./kriegsgef./…)."""
    vzor = re.compile(r"\b(" + "|".join(re.escape(p) for p in prijmeni) + r")\b", re.I)
    for m in vzor.finditer(text):
        okno = text[m.start(): m.start() + 320]
        rj = (re.match(r"^(\S+\s+[^.,_…:\d]{1,25}?)\s*[._…:]{3,}\s*(\d{1,4})?", okno)
              or re.match(r"^(\S+\s+[\w-]+)\s*\.\s*(\d{1,4})\b", okno)
              or re.match(r"^(\S+\s+[\w-]+)\s+(\d{1,4})\s+[A-ZÁ-Ž]", okno))
        if rj:   # rejstřík ztrátových seznamů: „Příjmení Jméno ..... 603“ = číslo strany se zápisem
            yield {"text": f"{rj.group(1)} → rejstřík" + (f", str. {rj.group(2)}" if rj.group(2) else ""), "rok": None, "stav": "rejstřík"}
            continue
        k = STAV_RE.search(okno, 10)
        z = okno[: k.end()] if k else okno[:200]
        roky = re.findall(r"\b(18[4-9]\d|190\d|191\d)\b", z)
        stav = next((cz for de, cz in STAV if k and k.group(1).lower().startswith(de)), "?")
        yield {"text": z.strip(" ;,"), "rok": int(roky[-1]) if roky else None, "stav": stav}


def kramerius(prijmeni, jmeno, rok=None, obce=(), rows=100, vystup=None, rejstriky=False, limit=40):
    ps, js = varianty(prijmeni, jmeno)
    terms = [f'"{p} {j}"' if j else f'"{p}"' for p in ps for j in js]
    q = "text_ocr:(" + " OR ".join(terms) + ") AND root_title:Verlust* AND fedora.model:page"
    prm = {"q": q, "fl": "PID,root_title,datum_str,dostupnost", "rows": rows, "wt": "json"}
    docs, start, total = [], 0, None
    try:
        while total is None or start < min(total, 600):
            d = json.loads(_get(API + "search?" + urllib.parse.urlencode({**prm, "start": start})))
            total = d["response"]["numFound"]
            docs += d["response"]["docs"]; start += rows
    except Exception as e:
        print(f"Kramerius nedostupný ({e}). Přidej doménu kramerius5.nkp.cz do allowlistu, nebo hledej ručně na kramerius.nkp.cz.")
        return []
    docs = [x for x in docs if x.get("dostupnost") != "private"]
    print(f"Kramerius – ztrátové seznamy: {d['response']['numFound']} stran, veřejných {len(docs)}; čtu jejich text…")
    obce_v = set()
    for o in obce:
        if o: obce_v |= {o, OBCE_DE.get(o, o)}
    jm = [j for j in js if j]
    nalez, videno = [], set()

    def stahni(x):
        try: return x, ocr(x["PID"])
        except Exception as e: return x, ""
    with ThreadPoolExecutor(6) as ex:
        for x, t in ex.map(stahni, docs):
            for z in zaznamy(t, ps):
                hlava = z["text"][:45]
                if jm and not any(podobne(w, j) for w in re.findall(r"\w+", hlava)[1:3] for j in jm):
                    continue
                klic = (bez_diakritiky(z["text"][:60]).lower(), z["rok"])
                if klic in videno: continue
                videno.add(klic)
                skore = 0
                if rok and z["rok"]: skore += 2 if abs(z["rok"] - rok) <= 1 else -2
                slova = re.findall(r"[\w-]+", z["text"])
                slova += [a + b for a, b in zip(slova, slova[1:])]   # OCR rozdělí „Schlan“ na „Schi an“
                if obce_v and any(podobne(w, o, 0.82) for w in slova for o in obce_v): skore += 3
                nalez.append({**z, "skore": skore, "datum": x.get("datum_str"), "pid": x["PID"]})
    nalez.sort(key=lambda z: (-z["skore"], z["rok"] or 0))
    rej = [z for z in nalez if z["stav"] == "rejstřík"]
    zap = [z for z in nalez if z["stav"] != "rejstřík"]
    print(f"Nalezeno {len(zap)} zápisů a {len(rej)} řádků rejstříku" + (" – řazeno podle shody s rokem narození a obcí" if rok or obce_v else "") + ":\n")
    for z in (nalez if rejstriky else zap)[:limit]:
        hv = "★★★" if z["skore"] >= 5 else "★★" if z["skore"] >= 3 else "★" if z["skore"] >= 2 else "  "
        print(f"{hv} {z['datum'] or '?':>10} | {z['stav']:<9} | nar. {z['rok'] or '?'} | {z['text'][:170]}")
        print(f"      https://kramerius.nkp.cz/view/{z['pid']}")
    if len(zap) > limit and not rejstriky: print(f"… a dalších {len(zap) - limit} (vše v --vystup souboru)")
    if rej and not rejstriky: print(f"Rejstříky ({len(rej)}) ukáže --rejstriky; čísla stran vedou k zápisům, které OCR nenašlo.")
    if nalez and (rok or obce_v):
        print("\n★★★ = sedí rok narození i obec, ★★ = sedí obec, ★ = sedí rok. OCR je chybové – zápis vždy ověř na snímku.")
    if vystup:
        with open(vystup, "w", encoding="utf-8") as f:
            f.write(f"# Ztrátové seznamy: {jmeno} {prijmeni}\n\n| shoda | vydáno | osud | nar. | zápis (OCR) | odkaz |\n|---|---|---|---|---|---|\n")
            for z in nalez:
                f.write(f"| {z['skore']} | {z['datum']} | {z['stav']} | {z['rok'] or ''} | {z['text'][:200].replace('|', '/')} | [snímek](https://kramerius.nkp.cz/view/{z['pid']}) |\n")
        print(f"\nUloženo: {vystup}")
    return nalez


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prijmeni"); ap.add_argument("jmeno", nargs="?", default="")
    ap.add_argument("--narozen"); ap.add_argument("--obec", action="append", default=[], help="domovská obec nebo okres (lze opakovat; česky – německý název se doplní)")
    ap.add_argument("--obec-de", action="append", default=[], help="německý název obce, pokud není v OBCE_DE")
    ap.add_argument("--kramerius", action="store_true", help="prohledat a rozebrat ztrátové seznamy 1914–1919")
    ap.add_argument("--rejstriky", action="store_true", help="vypsat i řádky z rejstříků (jméno → strana)")
    ap.add_argument("--vystup", help="uložit nálezy jako Markdown tabulku (např. pracovni/valky_fleischmann.md)")
    a = ap.parse_args()
    ps, js = varianty(a.prijmeni, a.jmeno)
    print(f"Hledáno: {a.jmeno} {a.prijmeni}" + (f", * {a.narozen}" if a.narozen else "") + (f", {', '.join(a.obec)}" if a.obec else ""))
    print("Varianty příjmení:", ", ".join(ps), "| jména:", ", ".join(j for j in js if j))
    rok = int(a.narozen) if a.narozen and a.narozen.isdigit() else None
    if rok is None or 1850 <= rok <= 1903:
        print("\n1. světová válka (narození cca 1850–1903):")
        print("  - VÚA databáze VHA (padlí, legionáři): https://www.vuapraha.cz/databaze-vha – příjmení + jméno, porovnej rok a domovskou obec")
        print("  - Evidence válečných hrobů: https://evidencevh.army.cz – stačí příjmení")
        print("  - Ztrátové seznamy: tento skript s --kramerius (OCR, zkus i německé tvary)")
    if rok is None or rok >= 1860:
        print("\n2. světová válka / holocaust:")
        print("  - Databáze obětí holocaust.cz: https://www.holocaust.cz/databaze-obeti/ – jméno, datum narození, transporty, dokumenty")
        print("  - Yad Vashem: https://collections.yadvashem.org/en/names – i svědecké listy (Page of Testimony) od příbuzných")
        print("  - Arolsen Archives: https://collections.arolsen-archives.org – karty z táborů, nucené práce, DP po válce")
        print("  - EHRI: https://portal.ehri-project.eu – oběti Terezína a archivy (např. Židovské muzeum)")
        print("  - Volksbund Gräbersuche: https://www.volksbund.de/erinnern-gedenken/graebersuche-online – padlí ve wehrmachtu")
        print("  - VÚA: příslušníci čs. jednotek v zahraničí, padlí 1939–45 – https://www.vuapraha.cz")
    if a.kramerius:
        print(); kramerius(a.prijmeni, a.jmeno, rok, a.obec + a.obec_de, vystup=a.vystup, rejstriky=a.rejstriky)


if __name__ == "__main__":
    main()
