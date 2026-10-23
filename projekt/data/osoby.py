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
 1: dict(n="Dominik Kulich", y="* 1995", st="fam", sex="M", f=["* 1995 Litoměřice", "bydliště Chudoslavice čp. 26 (rodinný údaj, potvrzeno 23. 10. 2026)"], r=[],
         note="Žijící – současné bydliště doplněno na výslovnou žádost Dominika. Bydliště v Chudoslavicích čp. 26 sdělil Dominik 23. 10. 2026 a výslovně požádal o doplnění na web. Jde o současný rodinný údaj, nikoli matriční doklad nebo datum nastěhování."),
 2: dict(n="Luboš Kulich", y="* 1962", st="fam", f=["* 1962 Roudnice nad Labem (?)", "od dětství v Horních Beřkovicích"], r=[],
         note="Žijící – údaje jen základní. Místo narození podle Dominika nejisté (Roudnice?)."),
 3: dict(n="Jana Poláková", y="* 1964", st="fam", f=["* 1964 Moravská Třebová", "bydliště Chudoslavice čp. 26 (rodinný údaj, potvrzeno 23. 10. 2026)"], r=[],
         note="Žijící – současné bydliště doplněno na výslovnou žádost Dominika. Bydliště v Chudoslavicích čp. 26 sdělil Dominik 23. 10. 2026 a výslovně požádal o doplnění na web. Jde o současný rodinný údaj, nikoli matriční doklad nebo datum nastěhování."),
 4: dict(n="Václav Kulich", y="asi 1936 – asi 2000", st="fam", f=["* asi 1936 Ledčice (?)", "zedník, stavěl paneláky", "Ledčice čp. 85 (?)", "† asi 2000"], r=[],
         note="Podle Dominika: z Ledčic (nejisté), narozen asi 1936. V katastru je „Václav Kulich, Ledčice čp. 85“ jako nedostatečně identifikovaný vlastník parcely v k. ú. Mnetěš – může to být on, nebo jeho otec stejného jména."),
 5: dict(n="Marcela Krsková", y="", st="fam", f=[], r=[],
         note="Rodinný strom (GenoPro, dokumenty/rodokmen.gno): „Marcela rozená Krsková, Kulichová“. Dominik si pamatoval „Trsková“."),
 6: dict(n="Miloslav Polák", y="1932 – asi 2014", st="fam", f=["* 1932 Čunín", "učitel autoškoly", "† asi 2014"], r=[],
         note="Otec Jany; ve stromu GenoPro „učitel autoškoly“ (potvrdil Dominik). Dominik 22. 10. 2026 definitivně potvrdil rodinné spojení s Františkem Polákem (*1905); rodiče vedeni jako František Polák a Františka Krejčí (sňatek 1929). Zdrojem potvrzení je rodinné sdělení, nikoli nově získaný rodný list."),
 12: dict(parent_link="fam", n="František Polák", y="* 1905", st="doc",
         f=["* 27. 12. 1905 Čunín čp. 26", "řezník v Čuníně čp. 26", "× 9. 11. 1929 Strážisko Františka Krejčí"],
         r=["cunin_krest_frantisek_polak_1905", "konice_snatek_frantisek_polak_frantiska_krejci_1929"],
         note="Údaje čteny ze snímků. Vazba na syna Miloslava (* 1932 Čunín): Dominik si pamatuje, že Miloslavovi rodiče byli František a Františka (20. 10. 2026), a jde o jediný sňatek Poláka z Čunína v rejstříku oddaných Konice 1893–1943 před r. 1932. Dominik 22. 10. 2026 označil toto spojení za definitivní; evidováno jako potvrzený údaj od rodiny. Číslo domu 26 je přímo čitelné v křtu 1905 i sňatku 1929. Stejné číslo má dům Kaštánkových v Dolní Rožínce a dnešní bydliště Dominika s maminkou v Chudoslavicích (rodinné sdělení 23. 10. 2026)."),
 13: dict(parent_link="fam", n="Františka Krejčí", y="* 1906", st="doc",
         f=["bydliště Konice (sčítání 1910 a 1921; číslo domu na výřezech neověřeno)", "* 10. 11. 1906 Olomouc (zemská porodnice)", "Konice čp. 233", "× 9. 11. 1929 Strážisko František Polák"],
         r=["konice_scitani_frantiska_krejci_1910", "konice_scitani_frantiska_krejci_1921", "konice_snatek_frantisek_polak_frantiska_krejci_1929"],
         note="Nemanželská dcera Filomeny Krejčí. Vazba na Miloslava jako u č. 12 (rodina: matka Miloslava se jmenovala Františka). Sčítací výřezy 1910 a 1921: Františka se shodným datem narození 10. 11. 1906 je uvedena v Konici jako nemanželská vnučka. Roku 1910 oprava vpravo uvádí narození v Olomouci. Roku 1921 vztah předběžně čteme jako nemanželské dítě dcery Fil. Krejčí. Totožnost silně podporuje oddací zápis 1929; data narození starších členů domácnosti zůstávají rozporná."),
 24: dict(n="Jan Polák", y="1865–1943", st="doc", f=["* 6. 6. 1865 Čunín čp. 64", "domkář, později zahradník v Čuníně čp. 26", "× 16. 2. 1892 Ptení Františka Bavlnková (2. sňatek, vdovec)", "† 11. 2. 1943 Kostelec (?)"],
         r=["cunin_krest_jan_polak_1865", "stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905", "konice_snatek_frantisek_polak_frantiska_krejci_1929", "cunin_krest_jan_polak_1893", "cunin_krest_vincencie_polakova_1894", "cunin_krest_ruzena_polakova_1896", "cunin_krest_arnost_polak_1899", "cunin_krest_josef_polak_1900", "cunin_krest_bohumila_polakova_1901", "cunin_krest_josef_polak_1904", "cunin_krest_marie_polakova_1908", "cunin_krest_frantiska_polakova_1912", "cunin_krest_antonin_polak_1914"],
         note="Otec Františka (doc z křtu 1905). Spojení s Miloslavem potvrdil Dominik 22. 10. 2026 (viz č. 12). V r. 1892 vdovec – první manželka zemřela před 29. 1. 1892 (úmrtní list z Konice). Křest Františka uvádí sňatek 9. 2. 1892, oddací matrika 16. 2. 1892."),
 25: dict(n="Františka Bavlnková", y="* 1870", st="doc", f=["* 19. 11. 1870 Stínava čp. 29", "1892 Stínava čp. 36", "× 16. 2. 1892 Ptení Jan Polák"],
         r=["stinava_krest_frantiska_bavlnkova_1870", "stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905", "konice_snatek_frantisek_polak_frantiska_krejci_1929", "cunin_krest_jan_polak_1893", "cunin_krest_vincencie_polakova_1894", "cunin_krest_ruzena_polakova_1896", "cunin_krest_arnost_polak_1899", "cunin_krest_josef_polak_1900", "cunin_krest_bohumila_polakova_1901", "cunin_krest_josef_polak_1904", "cunin_krest_marie_polakova_1908", "cunin_krest_frantiska_polakova_1912", "cunin_krest_antonin_polak_1914"],
         note="Matka Františka (doc z křtu 1905)."),
 48: dict(n="Jan Polák", y="1838–1915", st="doc", f=["* 10. 8. 1838 Křemenec čp. 32", "† 9. 3. 1915", "podruh v Křemenci, pak v Čuníně (1865, 1892), později zahradník/domkář", "× 18. 11. 1862 Konice Anna Pospíšilová"], r=["cunin_krest_frantisek_polak_1860", "cunin_krest_eduard_polak_1868", "cunin_krest_josefa_polakova_1872", "cunin_krest_marianna_polakova_1873", "cunin_krest_marie_polakova_1876", "cunin_krest_alois_polak_1878", "kremenec_krest_jan_polak_1838", "konice_snatek_jan_polak_anna_pospisilova_1862", "cunin_krest_jan_polak_1865", "stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905"],
         note="1892 „podruh z Čunína“, 1904 „domkář“, 1905 „zahradník“."),
 49: dict(n="Anna Pospíšilová", y="* asi 1835", st="doc", f=["* asi 1835", "z Čunína", "× 18. 11. 1862 Konice Jan Polák"], r=["cunin_krest_frantisek_polak_1860", "cunin_krest_eduard_polak_1868", "cunin_krest_josefa_polakova_1872", "cunin_krest_marianna_polakova_1873", "cunin_krest_marie_polakova_1876", "cunin_krest_alois_polak_1878", "konice_snatek_jan_polak_anna_pospisilova_1862", "cunin_krest_jan_polak_1865", "stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905"], note="Dcera Jiřího Pospíšila, domkaře v Čuníně, a Anny roz. Švedové (?)."),
 100: dict(n="Antonín Bavlnka", y="", st="prob", f=["podruh z Prostějoviček"], r=["stinava_krest_frantiska_bavlnkova_1870"], note="Dědeček Františky Bavlnkové."),
 101: dict(n="Josefa Nezvalová", y="", st="prob", f=["z Prostějoviček"], r=["stinava_krest_frantiska_bavlnkova_1870"], note=""),
 102: dict(n="František Bureš", y="", st="prob", f=["podruh (1870), domkář (1892) ve Stínavě"], r=["stinava_krest_frantiska_bavlnkova_1870", "stinava_snatek_jan_polak_frantiska_bavlnkova_1892"], note=""),
 103: dict(n="Františka Jelínková", y="", st="prob", f=["z Hradiska"], r=["stinava_krest_frantiska_bavlnkova_1870"], note=""),
 96: dict(n="Martin Polák", y="* 1816", st="doc", f=["* 25. 10. 1816 Křemenec čp. 7", "× 18. 10. 1837 Konice Marianna Tilšerová", "zahradník v Křemenci (1838, 1865), 1862 výměnkář"], r=["kremenec_krest_martin_polak_1816", "kremenec_snatek_martin_polak_marianna_tilserova_1837", "kremenec_krest_jan_polak_1838", "konice_snatek_jan_polak_anna_pospisilova_1862", "cunin_krest_jan_polak_1865"], note="Syn sedláka (pololáníka) Jiřího Poláka z Křemence čp. 7. Při sňatku 1837 nezletilý, otec již nežil."),
 97: dict(n="Marianna Tilšerová", y="* asi 1812", st="doc", f=["* asi 1812 Veselá (Fröhlichsdorf) čp. 10", "× 18. 10. 1837 Konice Martin Polák"], r=["kremenec_snatek_martin_polak_marianna_tilserova_1837", "kremenec_krest_jan_polak_1838", "konice_snatek_jan_polak_anna_pospisilova_1862", "cunin_krest_jan_polak_1865"], note="Dcera familianta Jiřího Tilšera z Veselé; při sňatku 1837 25 let. Příjmení potvrzeno oddací matrikou 1837 a křtem syna 1838."),
 98: dict(n="Jiří Pospíšil", y="", st="prob", f=["domkář v Čuníně (1865), 1862 uvedeno Bílsko (?)"], r=["konice_snatek_jan_polak_anna_pospisilova_1862", "cunin_krest_jan_polak_1865"], note=""),
 194: dict(n="Jiří Tilšer", y="", st="doc", f=["familiant ve Veselé (Fröhlichsdorf) čp. 10"], r=["kremenec_snatek_martin_polak_marianna_tilserova_1837", "kremenec_krest_jan_polak_1838", "konice_snatek_jan_polak_anna_pospisilova_1862"], note="Otec Marianny (sňatek 1837, křest vnuka 1838)."),
 195: dict(n="Barbora Hirthová (?)", y="", st="prob", f=[], r=["kremenec_snatek_martin_polak_marianna_tilserova_1837"], note="Matka Marianny Tilšerové; rodné příjmení čteno nejistě („Hirth“) – ze sňatku dcery 1837."),
 192: dict(n="Jiří Polák", y="* 1786", st="doc", f=["* (křest) 20. 4. 1786 Křemenec čp. 7", "sedlák (pololáník) v Křemenci čp. 7", "× 28. 1. 1812 Konice Marianna Paulíková", "† před 1837"], r=["kremenec_krest_jiri_polak_1786", "kremenec_snatek_jiri_polak_marianna_paulikova_1812", "kremenec_krest_martin_polak_1816", "kremenec_snatek_martin_polak_marianna_tilserova_1837"], note="Syn zemřelého Josefa Poláka, sedláka z Křemence; při sňatku 1812 26 let."),
 193: dict(n="Marianna Paulíková", y="* asi 1790", st="doc", f=["* asi 1790 Čunín čp. 9", "× 28. 1. 1812 Konice Jiří Polák"], r=["kremenec_snatek_jiri_polak_marianna_paulikova_1812", "kremenec_krest_martin_polak_1816", "kremenec_snatek_martin_polak_marianna_tilserova_1837"], note="Dcera sedláka Václava Paulíka z Čunína čp. 9; při sňatku 1812 22 let."),
 384: dict(n="Josef Polák", y="", st="doc", f=["sedlák v Křemenci čp. 7", "× 4. 7. 1779 Konice Anna Popelková", "† před 1812"], r=["kremenec_snatek_josef_polak_anna_popelkova_1779", "kremenec_krest_jiri_polak_1786", "kremenec_snatek_jiri_polak_marianna_paulikova_1812"], note="Syn Josefa Poláka z Křemence. Sňatek 1779 (latinsky), křest syna Jiřího 1786, zemřelý při sňatku syna 1812."),
 385: dict(n="Anna Popelková", y="", st="doc", f=["z Budětska", "× 4. 7. 1779 Konice Josef Polák"], r=["kremenec_snatek_josef_polak_anna_popelkova_1779", "kremenec_krest_jiri_polak_1786"], note="Dcera Pavla Popelky z Budětska."),
 768: dict(n="Josef Polák", y="", st="prob", f=["Křemenec"], r=["kremenec_snatek_josef_polak_anna_popelkova_1779"], note="Otec ženicha Josefa ve sňatku 1779 – nejstarší známý Polák."),
 770: dict(n="Pavel Popelka", y="", st="prob", f=["Budětsko"], r=["kremenec_snatek_josef_polak_anna_popelkova_1779"], note="Otec nevěsty Anny ve sňatku 1779."),
 386: dict(n="Václav Paulík", y="", st="prob", f=["sedlák v Čuníně čp. 9"], r=["kremenec_snatek_jiri_polak_marianna_paulikova_1812", "kremenec_krest_martin_polak_1816"], note="Ze sňatku dcery 1812 a křtu vnuka 1816."),
 198: dict(n="Josef Švéda", y="", st="prob", f=["domkář ve Studénkách"], r=["konice_snatek_jan_polak_anna_pospisilova_1862"], note="Otec Anny Švedové; čtení nejisté."),
 99: dict(n="Anna Švédová", y="", st="prob", f=["ze Studének"], r=["konice_snatek_jan_polak_anna_pospisilova_1862", "cunin_krest_jan_polak_1865"], note="Dcera Josefa Švédy, domkáře ve Studénkách (čteno ve křtech vnoučat 1868–1878)."),
 50: dict(n="Antonín Bavlnka", y="", st="prob", f=["domkař ve Stínavě (čp. 29, 1892 čp. 36)", "syn podruha z Prostějoviček"], r=["stinava_krest_frantiska_bavlnkova_1870", "stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905"], note=""),
 51: dict(n="Františka Burešová", y="", st="prob", f=["ze Stínavy"], r=["stinava_krest_frantiska_bavlnkova_1870", "stinava_snatek_jan_polak_frantiska_bavlnkova_1892", "cunin_krest_frantisek_polak_1905"], note="Dcera Františka Bureše, domkaře ze Stinavy."),
 26: dict(n="otec neuveden", st="unk", f=[], note="Františka Krejčí je nemanželská dcera Filomeny Krejčí; otec v oddacím zápisu neuveden."),
 27: dict(n="Filomena Krejčí", y="", st="prob", f=["Konice"], r=["konice_scitani_frantiska_krejci_1910", "konice_scitani_frantiska_krejci_1921", "konice_snatek_frantisek_polak_frantiska_krejci_1929"],
         note="Svobodná matka Františky; dcera Františka Krejčího, domkáře v Konici, a Františky. Křest Filomeny zatím nenalezen – v rejstřících Konice 1870–1887 jsou 3 Filomeny Krejčí (1871 Konice str. 26?, 1881 Michnov, 1885 Klužínek); otec není jistý, rozhodne oddací/křestní zápis Františky 1906 (Olomouc) nebo křest Filomeny. Sčítání 1921: u Františky (*10. 11. 1906) předběžně čteme „nem. dítě dcery Fil. Krejčí“. Podporuje spojení Filomeny s domácností Františka a Františky Krejčích, kteří jsou uvedeni i ve sčítání 1910. Filomena sama na těchto výřezech není. Rozdílná narození staršího páru zatím nerozhodnuta; nové osoby podle nich neztotožňujeme jako jisté."),
 7: dict(n="Jana Helena Kaštánková", y="", st="fam", f=["švadlena"], r=[],
         note="Matka Jany; ze stromu GenoPro („JanaHelena rozená Kaštánková, Poláková“)."),
 14: dict(n="Václav Kaštánek", y="* 1914", st="doc", f=["* 15. 9. 1914 Dolní Rožínka čp. 26", "× 19. 10. 1941 Zvole Helena Šlosárová", "později Bratrušín (u Bystřice nad Pernštejnem)"], r=["rozinka_krest_vaclav_kastanek_1914"],
         note="Otec Jany Heleny. Křest: N Zvole kn. 16569, sn. 215, č. 13; přípisek o sňatku s Helenou Šlosárovou potvrzuje, že jde o něj. Bratrušín (sdělil Dominik 22. 10. 2026) je obec farnosti Bystřice nad Pernštejnem vedle Domanína. Číslo domu 26 je přímo čitelné v křtu 1914. Stejné číslo má dům Polákových v Čuníně a dnešní bydliště Dominika s maminkou v Chudoslavicích (rodinné sdělení 23. 10. 2026)."),
 15: dict(n="Helena Šlosárová", y="* 1920", st="fam", f=["* 20. 10. 1920 Malý Lapáš (okres Nitra, Slovensko)", "služka", "× 19. 10. 1941 Zvole Václav Kaštánek"], r=["rozinka_krest_vaclav_kastanek_1914"],
         note="Matka Jany Heleny. Možná křtěna jako Elena (slovensky) – podle Dominika; na Slovensku hledat Elena/Helena/Ilona, příjmení Šlosár/Šlosárová/Schlosser/Szlosár. Datum a místo narození sdělil Dominik 22. 10. 2026; sňatek z přípisku u křtu Václava. Slovenské matriky – Štátny archív v Nitre / FamilySearch."),
 28: dict(n="Ignác Kaštánek", y="1878–1952", st="doc", f=["* 25. 4. 1878 Domanín čp. 15", "čeledín v Domaníně čp. 32 (1903), kočí v Dolní Rožínce (1914)", "× 4. 5. 1903 Bystřice Josefa Vykutilová", "× 5. 7. 1923 Rozsochy Albína Šmerdová (?) (2. sňatek)", "× 16. 10. 1934 Rozsochy Růžena Vaší…ová (?) (3. sňatek)", "† 9. 5. 1952 Bratrušín", "Dolní Rožínka čp. 26 (rodina doložena křtem syna Václava 1914)"],
         r=["domanin_krest_ignac_kastanek_1878", "bystrice_snatek_ignac_kastanek_josefa_vykutilova_1903", "rozinka_krest_vaclav_kastanek_1914", "rozinka_krest_bozena_kastankova_1905", "rozinka_krest_josef_vincenc_kastanek_1908", "rozinka_krest_ignac_kastanek_1910", "rozinka_krest_hubert_kastanek_1912", "rozinka_krest_josef_kastanek_1919"],
         note="Křest Domanín 1878 (N Bystřice obce kn. 15440, sn. 114) s přípisky o třech sňatcích a úmrtí. Sňatek 1903 i křest syna 1914 uvádějí narození 26. 4. – podle křestní matriky 25. 4. (26. 4. = křest)."),
 29: dict(n="Josefa Vykutilová", y="* 1880", st="doc", f=["* 25. 12. 1880", "služka v Bystřici čp. 337 (1903)", "× 4. 5. 1903 Bystřice Ignác Kaštánek", "Dolní Rožínka čp. 26 (rodina doložena křtem syna Václava 1914)"], r=["bystrice_snatek_ignac_kastanek_josefa_vykutilova_1903", "rozinka_krest_vaclav_kastanek_1914", "rozinka_krest_bozena_kastankova_1905", "rozinka_krest_josef_vincenc_kastanek_1908", "rozinka_krest_ignac_kastanek_1910", "rozinka_krest_hubert_kastanek_1912", "rozinka_krest_josef_kastanek_1919"],
         note="Příjmení potvrzeno oddací matrikou 1903 (ve křtu syna 1914 nečitelně „Oyketila“). Při sňatku nezletilá – svolil otec."),
 56: dict(n="Ignác Kaštánek", y="", st="doc", f=["podruh v Domaníně (1878, 1903)", "† před 1903"], r=["domanin_krest_ignac_kastanek_1878", "bystrice_snatek_ignac_kastanek_josefa_vykutilova_1903", "rozinka_krest_vaclav_kastanek_1914"], note="Ze křtu syna 1878, sňatku syna 1903 a křtu vnuka 1914. Syn Karla Kaštánka, podruha v Domaníně."),
 57: dict(n="Františka Hradešínská", y="", st="doc", f=["dcera domkáře z Blažovic", "žila 1903"], r=["domanin_krest_ignac_kastanek_1878", "bystrice_snatek_ignac_kastanek_josefa_vykutilova_1903", "rozinka_krest_vaclav_kastanek_1914"], note="Ze křtu syna 1878, sňatku syna 1903 a křtu vnuka 1914."),
 58: dict(n="František Vykutil", y="", st="doc", f=["podruh v Bystřici (1903)", "nádeník v Bystřici (1914)"], r=["bystrice_snatek_ignac_kastanek_josefa_vykutilova_1903", "rozinka_krest_vaclav_kastanek_1914"], note="Ze sňatku dcery 1903 (svolil k němu) a křtu vnuka 1914."),
 59: dict(n="Kateřina Kroutilová", y="", st="doc", f=["† před 1903"], r=["bystrice_snatek_ignac_kastanek_josefa_vykutilova_1903", "rozinka_krest_vaclav_kastanek_1914"], note="Ze sňatku dcery 1903 a křtu vnuka 1914."),
 112: dict(n="Karel Kaštánek", y="", st="prob", f=["podruh v Domaníně"], r=["domanin_krest_ignac_kastanek_1878"], note="Ze křtu vnuka Ignáce 1878."),
 113: dict(n="Terezie", y="", st="prob", f=[], r=["domanin_krest_ignac_kastanek_1878"], note="Manželka Karla Kaštánka; rodné příjmení ve křtu vnuka 1878 přepsané přípiskem – zjistit ze sňatku nebo křtu syna Ignáce st."),
 114: dict(n="Josef Hradešínský", y="", st="prob", f=["domkář v Blažovicích"], r=["domanin_krest_ignac_kastanek_1878"], note="Ze křtu vnuka Ignáce 1878."),
 115: dict(n="Josefa Žilková", y="", st="prob", f=[], r=["domanin_krest_ignac_kastanek_1878"], note="Ze křtu vnuka Ignáce 1878."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
 8: ("Kulichové", "Rod po meči. Děda Václav Kulich (* asi 1936) pocházel z Ledčic u Roudnice nad Labem, kde rodina žila v čp. 85; byl zedník a stavěl paneláky."),
 12: ("Polákové", "Drobní zahradníci, domkáři a řezníci z Čunína u Konice na Prostějovsku – doloženi od poloviny 19. století, dům čp. 26."),
 13: ("Krejčí", "Rod z Konice; Františka Krejčí (* 1906) byla vnučkou konického domkáře Františka Krejčího."),
 14: ("Kaštánkové", "Rod babičky Jany Heleny Kaštánkové; pradědeček Václav Kaštánek se narodil 1914 v Dolní Rožínce čp. 26 na Vysočině jako syn kočího Ignáce Kaštánka; starší rodová větev vede do Domanína u Bystřice nad Pernštejnem."),
 15: ("Šlosárovi", "Prababička Helena Šlosárová, narozená 1920 v Malém Lapáši u Nitry na Slovensku, služka."),
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
 dict(k=12, n="Jan Polák (* 16. 4. 1893), syn Eduarda", t="Bratranec Františka Poláka (*1905) a lednového Jana (*17. 1. 1893). Narozen v Čuníně čp. 71, křest 17. 4.; rodiče Eduard Polák a Filomena. Otcovi rodiče Jan Polák a Anna Pospíšilová přímo doloženi v rodném zápisu. Není dosud ztotožněn s padlým z čunínského pomníku.", r=["cunin_krest_jan_polak_1893_eduard"]),
 dict(k=12, n="Marie Trnková (* asi 1862)", t="Matka legionáře Františka Poláka (* 1890), dcera Josefa Trnky, domkáře v Čuníně, a Anny (její rodné příjmení zatím neověřeno). Sňatek s Františkem Polákem 17. 10. 1887; tehdy 25 let a 7 měsíců. Datum narození odhadnuto z věku, přesný křest dosud nemáme.", r=["cunin_snatek_frantisek_polak_marie_trnkova_1887", "cunin_krest_frantisek_polak_1890_legionar"]),
 dict(k=12, n="František Polák (* 1890), legionář", t="Bratranec Františka Poláka (* 1905). Narozen 4. 7. 1890 v Čuníně čp. 13, syn Františka Poláka a Marie Trnkové; prarodiče Jan Polák a Anna Pospíšilová. Krejčí, domovsky Prostějov. Zajat 2. 3. 1915 v Karpatech, od 24. 5. 1917 u 1. střeleckého pluku československých legií, demobilizován 8. 7. 1920. Spojení větve s Miloslavem (*1932) potvrdil Dominik 22. 10. 2026 jako definitivní rodinný údaj.", r=["cunin_krest_frantisek_polak_1890_legionar", "legie_frantisek_polak_1890"]),
 dict(k=24, n="František Polák (* 1860)", t="Nejstarší bratr Jana (* 1865); narozen 18. 10. 1860 v Čuníně čp. 64 jako nemanželský syn Anny Pospíšilové, legitimován sňatkem rodičů 18. 11. 1862 (přípisek v N Konice kn. 9077, sn. 101 – otec Jan Polák se k němu přihlásil). Domkář v Čuníně čp. 25, oženil se 17. 10. 1887 v Konici s Marií Trnkovou z Čunína čp. 30; otec legionáře Františka (* 1890).", r=["cunin_krest_frantisek_polak_1860", "cunin_snatek_frantisek_polak_marie_trnkova_1887", "cunin_krest_frantisek_polak_1890_legionar"]),
 dict(k=24, n="Eduard Polák (1868–1923)", t="Bratr Jana (* 1865); narozen 16. 11. 1868 v Čuníně čp. 64 (N Konice kn. 9079, sn. 93), zemřel 25. 7. 1923 (přípisek). Oženil se 19. 5. 1891 v Konici s Filomenou Hrušákovou (?) ze Strážiska; jako nezletilému dal souhlas otec Jan Polák. Syn Jan * 16. 4. 1893 (Čunín čp. 71).", r=["cunin_krest_eduard_polak_1868", "cunin_krest_jan_polak_1893_eduard"]),
 dict(k=24, n="Josefa Poláková (1872)", t="Sestra Jana (* 1865); narozena 19. 3. 1872 v Čuníně čp. 25 (N Konice kn. 9079, sn. 105), zemřela jako nemluvně 1872.", r=["cunin_krest_josefa_polakova_1872"]),
 dict(k=24, n="Marianna Poláková (1873)", t="Sestra Jana (* 1865); narozena 24. 12. 1873 v Čuníně čp. 25 (N Konice kn. 9079, sn. 111), zemřela jako nemluvně.", r=["cunin_krest_marianna_polakova_1873"]),
 dict(k=24, n="Marie Poláková (1876)", t="Sestra Jana (* 1865); narozena 6. 4. 1876 v Čuníně čp. 25 (N Konice kn. 9080, sn. 99), zemřela týž den.", r=["cunin_krest_marie_polakova_1876"]),
 dict(k=24, n="Alois Polák (1878)", t="Bratr Jana (* 1865); narozen 13. 12. 1878 v Čuníně čp. 25 (N Konice kn. 9080, sn. 88), zemřel týž den.", r=["cunin_krest_alois_polak_1878"]),
 dict(k=12, n="Jan Polák (* 1893)", t="Bratr Františka; narozen 17. 1. 1893 v Čuníně čp. 25 (N Konice kn. 9083 (Čunín 1893–1905), sn. 222); oddací zápis potvrzuje sňatek 31. 8. 1915 v Přemyslovicích s Helenou Kmentovou (*10. 2. 1895). Tehdy vojín c. k. zeměbraneckého pluku č. 13, na dovolené v Čuníně. Jeho ztotožnění s padlým z pomníku dosud není doloženo.", r=["cunin_krest_jan_polak_1893", "premyslovice_snatek_jan_polak_helena_kmentova_1915"]),
 dict(k=12, n="Vincencie Poláková (* 1894)", t="Sestra Františka; narozena 1894 v Čuníně čp. 26 (N Konice kn. 9083 (Čunín 1893–1905), sn. 229); podle přípisku sezdána 1. 10. 1917 v Konici s Methodějem Veselým (?).", r=["cunin_krest_vincencie_polakova_1894"]),
 dict(k=12, n="Růžena Poláková (* 1896)", t="Sestra Františka; narozena 18. 12. 1896 v Čuníně čp. 26 (N Konice kn. 9083 (Čunín 1893–1905), sn. 236); podle přípisku sezdána 29. 8. 1921 v Konici s Bedřichem Kuplou (?).", r=["cunin_krest_ruzena_polakova_1896"]),
 dict(k=12, n="Arnošt Polák (1899)", t="Bratr Františka; narozen 12. 1. 1899 v Čuníně čp. 26 (N Konice kn. 9083 (Čunín 1893–1905), sn. 242), zemřel 13. 2. 1899.", r=["cunin_krest_arnost_polak_1899"]),
 dict(k=12, n="Josef Polák (1900)", t="Bratr Františka; narozen v červenci 1900 v Čuníně čp. 26 (N Konice kn. 9083 (Čunín 1893–1905), sn. 248), zemřel 23. 10. 1900.", r=["cunin_krest_josef_polak_1900"]),
 dict(k=12, n="Bohumila Poláková (1901–1959)", t="Sestra Františka; narozena 4. 10. 1901 v Čuníně čp. 26 (N Konice kn. 9083 (Čunín 1893–1905), sn. 253); zemřela 14. 1. 1959 v Senici na Hané (přípisek).", r=["cunin_krest_bohumila_polakova_1901"]),
 dict(k=12, n="Josef Polák (1904–1905)", t="Bratr Františka; narozen v lednu 1904 v Čuníně čp. 26 (N Konice kn. 9083 (Čunín 1893–1905), sn. 260), zemřel 19. 2. 1905.", r=["cunin_krest_josef_polak_1904"]),
 dict(k=12, n="Marie Poláková (1908–1912)", t="Sestra Františka; narozena 9. 3. 1908 v Čuníně čp. 26 (N Konice kn. 9084 (Čunín 1906–1922), sn. 266), zemřela 28. 1. 1912.", r=["cunin_krest_marie_polakova_1908"]),
 dict(k=12, n="Františka Poláková (* 1912)", t="Sestra Františka; narozena 10. 3. 1912 v Čuníně čp. 26 (N Konice kn. 9084 (Čunín 1906–1922), sn. 280); podle přípisku oddána 23. 2. 1936 (Strážisko?).", r=["cunin_krest_frantiska_polakova_1912"]),
 dict(k=12, n="Antonín Polák (* 1914)", t="Bratr Františka; narozen 26. 2. 1914 v Čuníně čp. 26 (N Konice kn. 9084 (Čunín 1906–1922), sn. 285); oddán 18. 10. 1941 v Konici s Annou Hýblovou.", r=["cunin_krest_antonin_polak_1914"]),
 dict(k=3, n="Pavel Polák", t="Bratr Jany (Dominikův strýc). Havíř.", r=[]),
 dict(k=2, n="Marcela Kulichová", t="Sestra Luboše (Dominikova teta).", r=[]),
 dict(k=14, n="Božena Kaštánková (* 1905)", t="Sestra Václava; narozena 7. 10. 1905 v Dolní Rožínce čp. 26 (Matrika N Zvole kn. 16569, oddíl Dolní (Zámecká) Rožínka, sn. 131); kmotra Ludmila Vykutilová, svobodná nádenice v Bystřici (asi sestra matky); biřmována 1. 6. 1922 v Rozsochách; přípisek „Bystřice … 1934“ (asi sňatek).", r=["rozinka_krest_bozena_kastankova_1905"]),
 dict(k=14, n="Josef Vincenc Kaštánek (1908–1909)", t="Bratr Václava; narozen 28. 6. 1908 v Dolní Rožínce čp. 26 (Matrika N Zvole kn. 16569, oddíl Dolní (Zámecká) Rožínka, sn. 135), zemřel 1909.", r=["rozinka_krest_josef_vincenc_kastanek_1908"]),
 dict(k=14, n="Ignác (Hynek) Kaštánek (* 1910)", t="Bratr Václava; v rodině Hynek (česká podoba jména Ignác; podle Dominika 22. 10. 2026); narozen 25. 2. 1910 v Zámecké Rožínce čp. 26 (Matrika N Zvole kn. 16569, oddíl Dolní (Zámecká) Rožínka, sn. 207); biřmován 1. 6. 1922 v Rozsochách; podle přípisku oddán 22. 9. 1935 (nevěsta Marie Pl…ová?).", r=["rozinka_krest_ignac_kastanek_1910"]),
 dict(k=14, n="Hubert Kaštánek (* 1912)", t="Bratr Václava; narozen 28. 10. 1912 v Dolní Rožínce čp. 26 (Matrika N Zvole kn. 16569, oddíl Dolní (Zámecká) Rožínka, sn. 212); podle přípisku oddán 24. 10. 1935 s Helenou Vítkovou (?).", r=["rozinka_krest_hubert_kastanek_1912"]),
 dict(k=14, n="Josef Kaštánek (* 1919)", t="Bratr Václava; narozen 3. 3. 1919 v Dolní Rožínce (Matrika N Zvole kn. 16569, oddíl Dolní (Zámecká) Rožínka, sn. 218); biřmován 17. 6. 1929 v Rozsochách; oddán v Bystřici 24. 9. 1939 se Štěpánkou Škudovou (?).", r=["rozinka_krest_josef_kastanek_1919"]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
 ("Bojoval František Polák (*1890) u Zborova a na Transsibiřské magistrále?", "Otevřené: služba u 1. střeleckého pluku od 24. 5. 1917 do roku 1920 umožňuje tuto souvislost. Historie útvaru dokládá Zborov i ochranu magistrály, ale osobní účast Františka v konkrétních bojích zatím souhrnný záznam nepotvrzuje. Další pramen: legionářský poslužný spis."),
 ("Který Jan Polák z Čunína padl v roce 1915?", "Otevřené: pomník uvádí Jana Poláka 1893–1915. Matrika obsahuje dva Jany Poláky narozené 1893: 17. ledna, syn Jana a Františky Bavlnkové, a 16. dubna, syn Eduarda a Filomeny. Bez přesného data narození nebo rodičů v úmrtním/vojenském dokladu nelze padlého určit. Podrobnosti ve zprávě VALKY_2026-10-22.md."),
 ("Kdy se vzali Jan Polák a Františka Bavlnková?", "Vyřešeno: oddací matrika Ptení uvádí 16. 2. 1892; křestní zápis syna Františka (1905) chybně 9. 2. 1892."),
 ("Kdo byla první manželka Jana Poláka (* 1865) a měli děti?", "Otevřené: zemřela před 29. 1. 1892 (úmrtní list z fary Konice). V oddacích Čunína 1885–1891 sňatek není – nejspíš ve farnosti nevěsty. Hledat v zemřelých Konice 1888–1892."),
 ("Je František Polák (* 1905) otcem Miloslava Poláka (* 1932 Čunín)?", "Vyřešeno: Dominik 22. 10. 2026 definitivně potvrdil spojení svého dědečka Miloslava s Františkem Polákem (*1905). Zdrojem je rodinné potvrzení; jednotlivé starší osoby dokládají matriky."),
 ("Souvisí s námi Kulichové z Dolína u Slaného?", "Stopa: ztrátové seznamy 1915 uvádějí dva Antoníny Kulichy z Dolína (okres Slaný), nar. 1879 a 1888, oba v ruském zajetí. Dolín je asi 20 km od Ledčic. Ověřit, až budou známi předci dědy Václava (* asi 1936 Ledčice)."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
