# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
 1: dict(n="Dominik Kulich", y="* 1995", st="fam", sex="M", f=["* 1995 Litoměřice"], r=[],
         note="Žijící – údaje jen základní."),
 2: dict(n="Luboš Kulich", y="* 1962", st="fam", f=["* 1962 Roudnice nad Labem (?)", "od dětství v Horních Beřkovicích"], r=[],
         note="Žijící – údaje jen základní. Místo narození podle Dominika nejisté (Roudnice?)."),
 3: dict(n="Jana Poláková", y="* 1964", st="fam", f=["* 1964 Moravská Třebová"], r=[],
         note="Žijící – údaje jen základní."),
 4: dict(n="Václav Kulich", y="asi 1936 – asi 2000", st="fam", f=["* asi 1936 Ledčice (?)", "zedník, stavěl paneláky", "Ledčice čp. 85 (?)", "† asi 2000"], r=[],
         note="Podle Dominika: z Ledčic (nejisté), narozen asi 1936. V katastru je „Václav Kulich, Ledčice čp. 85“ jako nedostatečně identifikovaný vlastník parcely v k. ú. Mnetěš – může to být on, nebo jeho otec stejného jména."),
 5: dict(n="Marcela Krsková", y="", st="fam", f=[], r=[],
         note="Rodinný strom (GenoPro, dokumenty/rodokmen.gno): „Marcela rozená Krsková, Kulichová“. Dominik si pamatoval „Trsková“."),
 6: dict(n="Miloslav Polák", y="1932 – asi 2014", st="fam", f=["* 1932 Čunín", "učitel autoškoly", "† asi 2014"], r=[],
         note="Otec Jany; ve stromu GenoPro „učitel autoškoly“ (potvrdil Dominik). Rodiče pravděpodobně František Polák a Františka Krejčí (sňatek 1929) – ověřit rodným listem."),
 12: dict(n="František Polák", y="* 1905", st="prob",
         f=["* 27. 12. 1905 Čunín čp. 26", "řezník v Čuníně čp. 26", "× 9. 11. 1929 Strážisko Františka Krejčí"],
         r=["cunin_krest_frantisek_polak_1905", "konice_snatek_frantisek_polak_frantiska_krejci_1929"],
         note="Sňatek doložen (doc), ale že je to otec Miloslava (* 1932 Čunín), je odvozeno: jediný sňatek Poláka z Čunína v rejstříku oddaných Konice 1893–1943 před r. 1932. Potvrdí rodný list Miloslava."),
 13: dict(n="Františka Krejčí", y="* 1906", st="prob",
         f=["* 10. 11. 1906 Olomouc (zemská porodnice)", "Konice čp. 233", "× 9. 11. 1929 Strážisko František Polák"],
         r=["konice_snatek_frantisek_polak_frantiska_krejci_1929"],
         note="Nemanželská dcera Filomeny Krejčí. Vazba na Miloslava jako u č. 12."),
 24: dict(n="Jan Polák", y="* 1865", st="prob", f=["* 6. 6. 1865 Čunín (?)", "domkář, později zahradník v Čuníně čp. 26", "× 16. 2. 1892 Ptení Františka Bavlnková (2. sňatek, vdovec)"],
         r=["stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905", "konice_snatek_frantisek_polak_frantiska_krejci_1929"],
         note="Otec Františka (doc z křtu 1905). Linie k Miloslavovi prob (viz č. 12). V r. 1892 vdovec – první manželka zemřela před 29. 1. 1892 (úmrtní list z Konice). Křest Františka uvádí sňatek 9. 2. 1892, oddací matrika 16. 2. 1892."),
 25: dict(n="Františka Bavlnková", y="* 1870", st="prob", f=["* 19. 11. 1870 Stínava čp. 36 (?)", "ze Stínavy čp. 36", "× 16. 2. 1892 Ptení Jan Polák"],
         r=["stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905", "konice_snatek_frantisek_polak_frantiska_krejci_1929"],
         note="Matka Františka (doc z křtu 1905)."),
 48: dict(n="Jan Polák", y="", st="prob", f=["podruh, později zahradník/domkář v Čuníně"], r=["stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905"],
         note="1892 „podruh z Čunína“, 1904 „domkář“, 1905 „zahradník“."),
 49: dict(n="Anna Pospíšilová", y="", st="prob", f=["z Čunína"], r=["stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905"], note="Dcera Jiřího Pospíšila, domkaře v Čuníně."),
 50: dict(n="Antonín Bavlnka", y="", st="prob", f=["domkař ve Stínavě čp. 36"], r=["stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905"], note=""),
 51: dict(n="Františka Burešová", y="", st="prob", f=["ze Stínavy"], r=["stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905"], note="Dcera Františka Bureše, domkaře ze Stinavy."),
 26: dict(n="otec neuveden", st="unk", f=[], note="Františka Krejčí je nemanželská dcera Filomeny Krejčí; otec v oddacím zápisu neuveden."),
 27: dict(n="Filomena Krejčí", y="", st="prob", f=["Konice"], r=["konice_snatek_frantisek_polak_frantiska_krejci_1929"],
         note="Svobodná matka Františky; dcera Františka Krejčího, domkáře v Konici, a Františky."),
 7: dict(n="Jana Helena Kaštánková", y="", st="fam", f=["švadlena"], r=[],
         note="Matka Jany; ze stromu GenoPro („JanaHelena rozená Kaštánková, Poláková“)."),
 14: dict(n="Václav Kaštánek", y="", st="fam", f=["Dolní Rožínka"], r=[],
         note="Ze stromu GenoPro; u jména uvedena Dolní Rožínka. Vazba na Janu Helenu odvozena ze jmen – ověřit."),
 15: dict(n="Helena Šlosárová", y="", st="fam", f=["služka", "Lapáš (?)"], r=[],
         note="Ze stromu GenoPro („Helena rozená Šlosárová, Kaštánková, služka, Lapaš“)."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
 dict(k=24, n="Josef Polák (1904–1905)", t="Bratr Františka; narozen v lednu 1904 v Čuníně čp. 26, zemřel 1905.", r=[]),
 dict(k=3, n="Pavel Polák", t="Bratr Jany (Dominikův strýc). Havíř.", r=[]),
 dict(k=2, n="Marcela Kulichová", t="Sestra Luboše (Dominikova teta).", r=[]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
 ("Kdy se vzali Jan Polák a Františka Bavlnková?", "Vyřešeno: oddací matrika Ptení uvádí 16. 2. 1892; křestní zápis syna Františka (1905) chybně 9. 2. 1892."),
 ("Kdo byla první manželka Jana Poláka (* 1865) a měli děti?", "Otevřené: zemřela před 29. 1. 1892 (úmrtní list z fary Konice). Hledat sňatek v Konici asi 1886–1891 a úmrtí 1891–1892."),
 ("Je František Polák (* 1905) otcem Miloslava Poláka (* 1932 Čunín)?", "Hypotéza: jediný Polák z Čunína oddaný v Konici před 1932; potvrdí rodný list Miloslava."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
