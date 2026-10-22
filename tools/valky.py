#!/usr/bin/env python3
"""Hledání předků v databázích obětí a vojáků 1. a 2. světové války.

Použití (z kořene projektu):
  valky.py "Příjmení" [Jméno] [--narozen ROK] [--obec Obec] [--kramerius]
Vypíše připravené dotazy a odkazy do všech zdrojů (co a jak hledat) a s --kramerius rovnou prohledá
c. a k. ztrátové seznamy (Verlustliste 1914–1919) v Krameriu NK ČR – OCR, takže zkoušej i německé tvary
(Karl/Franz/Johann, Polak/Pollak, bez háčků).

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
import argparse, json, unicodedata, urllib.parse, urllib.request


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


def kramerius(prijmeni, jmeno, rows=40):
    ps, js = varianty(prijmeni, jmeno)
    terms = [f'"{p} {j}"'.replace(' "', '"') if j else f'"{p}"' for p in ps for j in js]
    q = "text_ocr:(" + " OR ".join(terms) + ") AND root_title:Verlust*"
    prm = {"q": q + " AND fedora.model:page", "fl": "PID,root_title,root_pid,datum_str,details", "rows": rows, "wt": "json",
           "hl": "true", "hl.fl": "text_ocr", "hl.fragsize": "220"}
    url = "https://kramerius5.nkp.cz/search/api/v5.0/search?" + urllib.parse.urlencode(prm)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "rodokmen-skill"}), timeout=90))
    except Exception as e:
        print(f"Kramerius nedostupný ({e}). Přidej doménu kramerius5.nkp.cz do allowlistu, nebo hledej ručně na kramerius.nkp.cz.")
        return
    hl = d.get("highlighting", {})
    print(f"Kramerius – ztrátové seznamy: {d['response']['numFound']} stran (dotaz {q})")
    for x in d["response"]["docs"]:
        h = " | ".join(hl.get(x["PID"], {}).get("text_ocr", []))[:300].replace("\n", " ")
        print(f"- {x.get('datum_str')} | {str(x.get('root_title'))[:50]} | https://kramerius.nkp.cz/view/{x['PID']}")
        if h: print("    ", h)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prijmeni"); ap.add_argument("jmeno", nargs="?", default="")
    ap.add_argument("--narozen"); ap.add_argument("--obec"); ap.add_argument("--kramerius", action="store_true")
    a = ap.parse_args()
    ps, js = varianty(a.prijmeni, a.jmeno)
    print(f"Hledáno: {a.jmeno} {a.prijmeni}" + (f", * {a.narozen}" if a.narozen else "") + (f", {a.obec}" if a.obec else ""))
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
        print(); kramerius(a.prijmeni, a.jmeno)


if __name__ == "__main__":
    main()
