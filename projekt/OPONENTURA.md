# Oponentura rodokmenu — 22. října 2026

Aktualizace po následném sdělení uživatele: Dominik definitivně potvrdil spojení dědečka Miloslava (*1932) s Františkem Polákem (*1905). Vazba je nyní vedena jako potvrzená rodinou, nikoli jako nově doložená matrikou. Níže uvedené výhrady k této konkrétní vazbě popisují stav před tímto potvrzením. Legionář byl doplněn do zajímavostí, rodinné časové osy, knihy, stránky Poláků a Čunína; u Zborova a magistrály je oddělena historie jeho pluku od dosud nedoložené osobní bojové účasti.

Závěr: dobrý výzkumný základ, ale nikoli definitivně ověřený rodokmen. Kontrola konzistence sama neověřuje správnost čtení ani příbuzenství.

## Rozsah kontroly
Prošel jsem datový model, všech šest evidovaných zápisů a přepisů, všech šest uložených obrazových výřezů, výzkumný deník, export a kontrolní skript, hlavní stahovací skripty MZA a SOA Litoměřice, strukturu webu a jeho sestavení. Ostatní Python nástroje prošly syntaktickou kontrolou; jejich všechny režimy nebyly integračně spuštěny. Nové hromadné hledání v archivech neproběhlo. Přímé načtení stránky MZA přes webový nástroj nebylo dostupné, proto obrazová kontrola vychází z místních výřezů. Nejde o úplnou paleografickou revizi každého slova.

## Prioritní nálezy
1. **Vazba Miloslav Polák (1932) → František Polák (1905) a Františka Krejčí (1906) nemá přímý doklad.** Shoda jmen rodičů a jediný nalezený sňatek jsou silné vodítko, ne důkaz. Rodný list Miloslava je nejdůležitější další krok: na této vazbě stojí velká část staršího stromu. Zachováno doložení jednotlivých osob, přidáno samostatné označení nejisté vazby v datech, stromu a kartách.
2. **Václav Kaštánek → Jana Helena je podle vlastní poznámky odvozen pouze ze jmen.** Také označeno jako nepotvrzená vazba; ověřit spojnice v původním GenoPro nebo rodinný doklad.
3. **Přihlášení je vypnuté.** Patička původně slibovala neveřejnost, kterou export nezajišťoval. Text opraven. Statické soubory samy přístup neomezují; noindex není přístupová ochrana. Před zveřejněním musí být skutečně nastavena a otestována brána na konkrétním hostingu. Tento zásah nic nezveřejnil.
4. **Export generoval neplatnou konfiguraci nginx bez hesla.** Dvě položky default ve stejném map bloku. Opraveno na jedinou výchozí hodnotu. Ověřeny obě větve generátoru; běh nginx v Dockeru nebyl testován.
5. **Vedlejší příbuzní nemají citace.** František (sňatek 1887), Eduard (1891) a Josef (1904–1905) jsou popsáni jako nálezy, ale nemají vlastní evidované zápisy. Doplnit zápis, výřez a přepis. U Josefa zkontrolovat také účel k=24: text jej popisuje jako bratra Františka, nikoliv Jana; přesun nelze dělat bez rozhodnutí, zda k označuje sourozence nebo rodinnou skupinu.
6. **Nejistoty se v popularizačních textech mění v jistoty.** Ledčice a čp. 85 jsou u Václava nejisté, úvod a popis rodu však znějí kategoricky. Katastrální jmenovec nepotvrzuje identitu. Kostelec na Hané je upřesnění obecného Kostelce z přípisku; ověřit úmrtní zápis. Roky 1838 a 1835 jsou odhad z věku při sňatku, nikoliv narození doložená křtem.
7. **Rod Kulichových se z přehledu vyřazuje.** Export filtruje rody podle existence osoby 8–15; osoba 8 chybí. To vysvětluje rozdíl pěti definovaných a čtyř zobrazených rodů. Doporučená další úprava: karta rozpracované větve bez vymyšleného předka.

## Matriky
- Sňatek 1892: na uloženém oddacím výřezu čtu 16. února; v křtu syna 1905 je 9. února. Upřednostnění přímého oddacího zápisu je odůvodněné. Obě znění musí zůstat v přepisech.
- František 1905: narození 27. prosince, křest 28. prosince. Jan 1865: narození 6. června, křest 7. června. Františka 1870: narození 19. listopadu, křest 20. listopadu. Pole datum v záznamech N dnes znamená narození, přestože titul zní Křest. Při dalším rozvoji oddělit oba typy událostí.
- Sňatek 1929: základní jména a data odpovídají výřezu. Samotný záznam nedokládá narození Miloslava 1932.
- Sňatek 1862: datum 18. listopadu a věky 24 a 27 jsou s evidencí slučitelné. Příjmení Tilšer/Šveda, svědci a místní názvy zůstávají nejisté. Nedoporučuji odstraňovat otazníky.
- Výřezy často nemají hlavičky sloupců. Uchovávat také celou stranu a kontrolovat, zda jsou skutečně zahrnuty všechny přípisky.

## Skripty a provoz
- kontrola.py ověřuje reference, základní pole a přítomnost příloh, nikoli chronologii, skutečný obsah přepisů, pravdivost identifikace nebo správnost souřadnic. Doplněna upozornění na nejisté vazby a chybějící citace vedlejších příbuzných.
- mza_dz.py: metadata se rozpoznávají jen úvodním znakem <; HTML chyba může být mylně přijata jako DZI a následně způsobit pád regexu. Skládání dlaždic nepracuje s atributem Overlap; u zdrojů s nenulovým překryvem by vznikaly chybné švy. Nejde o doloženou chybu aktuálních šesti výřezů. Nutné ověřovat výsledný obraz.
- mza_dz.py a soal_zoomify.py: chybí robustní validace úrovně zmenšení a úklid při výjimce. Stažení vyžaduje curl/ImageMagick podle nástroje. V tomto prostředí ImageMagick nebyl nalezen, nové kompletní stažení nebylo testováno.
- package.json používá python3, který může na Windows ukazovat na systémový alias. Export zde prošel s explicitní cestou k funkčnímu Pythonu.
- Výsledný web je nyní v nadřazené složce web_rodokmen, včetně přímo otevíratelného index.html. Aktualizuje jej tools/export_local.py z projekt/web/dist; původní obsah zálohuje. Zdrojové soubory zůstávají v projekt/web/src.

## Doplnění po válečné rešerši 22. 10. 2026

- Doložen nový vedlejší příbuzný, legionář František Polák *4. 7. 1890. Matrika i ČsOL citovány samostatně; vazba na Miloslava *1932 zůstává nejistá jako před rešerší.
- Dva Janové Polákové narození 1893 v Čuníně brání jednoznačnému přiřazení padlého z pomníku. Lednový Jan je správně syn Jana a Františky Bavlnkové; dubnový Jan má rodiče Eduarda a Filomenu. Stávající lednový Jan proto nebyl přepisován na syna Eduarda.
- Opravy valky.py: číslo rejstříku označuje vydání, rok úmrtí se nepoužije jako narození, rozpoznávání poškozeného slova kriegsgefangen a hranice dalšího vojáka omezují falešné záměny. Pět regresních testů vychází ze skutečných chybových vzorů. Výsledky OCR nadále vyžadují čtení skenu.
- Kompletní rozsah hledání, pozitivní nález, vyloučené shody a neprohledané zdroje jsou ve VALKY_2026-10-22.md. Starší upozornění na chybějící citace vedlejších příbuzných je historický stav; průběžně je doplňuje současný výzkum.

## Provedené ověření
Export dat; kontrola konzistence bez chyb (s uvedenými upozorněními); syntaktická kontrola Python souborů; sestavení 87 stránek Astro; sestavení indexu Pagefind; zobrazení úvodu a stromu v prohlížeči a kliknutí na přiblížení. Nebyla provedena kompletní mobilní a tisková vizuální revize ani test nasazeného přihlášení.
