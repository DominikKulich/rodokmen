// Historická povolání a společenské vrstvy venkova (Morava 18.–20. stol.) – vysvětlivky pro web.
// rank: vyšší = majetnější vrstva (pro řazení). re: jak povolání poznat v textu faktů.
export const POVOLANI = [
  { k: 'sedlák', re: /sedl[áa]k|l[áa]n[íi]k|bauer/i, rank: 9, vrstva: 'majitelé gruntů',
    text: 'Majitel celého selského gruntu (usedlosti) s polnostmi – na Moravě se velikost měřila v lánech: celoláník, pololáník, čtvrtláník. Do roku 1848 robotoval vrchnosti se svým potahem (koňmi nebo voly). Nejvážnější vrstva vesnice, z ní se volili rychtáři a konšelé.' },
  { k: 'výměnkář', re: /výměnk|vyměnk|ausgeding/i, rank: 7, vrstva: 'majitelé gruntů',
    text: 'Starý hospodář, který předal statek dědici a „na výměnku“ si vyhradil doživotní byt (výměnek), stravu, dříví a třeba kus pole. Výměnek se zapisoval do pozemkových knih.' },
  { k: 'familiant', re: /familiant/i, rank: 6, vrstva: 'menší usedlíci',
    text: 'Usedlík na menší usedlosti vzniklé rozdělením panského (dvorského) pozemku – tzv. raabizací za Marie Terezie a Josefa II. Tak vznikaly i celé nové osady s německými jmény typu „…dorf“ – nejspíš i Veselá (Fröhlichsdorf) u Konice, kde žili Tilšerovi (ověřit v dějinách obce). Familiant platil vrchnosti nájem místo roboty.' },
  { k: 'zahradník', re: /zahradn[íi]k|gärtler|gartler/i, rank: 5, vrstva: 'menší usedlíci',
    text: 'Pozor – nejde o pěstitele květin. Na Moravě „zahradník“ znamenal drobného usedlíka: měl chalupu se zahradou a malým kusem pole, menší než sedlák. Robotoval pěšky (ručně), bez potahu. Často si přivydělával řemeslem nebo nádenickou prací.' },
  { k: 'domkář', re: /domk[aá][řr]|häusler/i, rank: 4, vrstva: 'menší usedlíci',
    text: 'Vlastnil domek (chalupu), ale skoro žádnou půdu. Živil se jako nádeník, řemeslník nebo pomocník u sedláků. Proti podruhovi měl výhodu vlastní střechy nad hlavou.' },
  { k: 'kočí', re: /(^|[^a-zá-ž])ko[čc][íi](?![a-zá-ž])|kutscher/i, rank: 3, vrstva: 'služebnictvo a námezdní práce',
    text: 'Vozka, který se staral o koně a jezdil s povozem – často ve službách velkostatku nebo zámku („panský kočí“), jako na zámku v Dolní Rožínce. Placený námezdní zaměstnanec, obvykle s bytem v panském domě.' },
  { k: 'podruh', re: /podruh|inmann|inwohner|inquilinus/i, rank: 2, vrstva: 'bezzemci',
    text: 'Bezzemek bez vlastního domu: bydlel „v podruží“ – v pronajaté světnici v cizí chalupě. Živil se prací za mzdu u sedláků, na panském nebo jako nádeník. Nejchudší usedlá vrstva vesnice; podruhy se stávali i mladší sourozenci, kteří nezdědili grunt.' },
  { k: 'nádeník', re: /nádeník|nadeník|taglöhner/i, rank: 2, vrstva: 'bezzemci',
    text: 'Dělník najímaný na den („na den“ = nádeník) – na polní práce, stavby, v lese. Bez stálého zaměstnání a bez půdy.' },
  { k: 'čeledín', re: /čeledín|čeled|knecht/i, rank: 1, vrstva: 'služebnictvo a námezdní práce',
    text: 'Mladý svobodný muž ve službě u sedláka nebo na dvoře – bydlel a jedl u hospodáře, smlouva se uzavírala obvykle na rok (od Hromnic). Typický začátek života pro syny podruhů a domkářů.' },
  { k: 'služka', re: /služk|služeb|magd/i, rank: 1, vrstva: 'služebnictvo a námezdní práce',
    text: 'Svobodná žena ve službě v cizí domácnosti nebo hospodářství, za byt, stravu a malou mzdu. Ve městech i na venkově běžná životní etapa dívek z chudších rodin až do sňatku.' },
  { k: 'řezník', re: /řezník|fleischer/i, rank: 6, vrstva: 'řemeslníci',
    text: 'Řemeslník – porážel dobytek a prodával maso. Do roku 1859 byl organizován v cechu; na vesnici často spojoval řeznictví s malým hospodářstvím nebo hostincem.' },
  { k: 'zedník', re: /zedník|maurer/i, rank: 4, vrstva: 'řemeslníci',
    text: 'Stavební řemeslník. Ve 20. století zedníci stavěli i panelová sídliště – typickou bytovou výstavbu 60.–80. let.' },
  { k: 'švadlena', re: /švadlen/i, rank: 4, vrstva: 'řemeslníci',
    text: 'Šička oděvů – samostatně, v krejčovské dílně nebo v oděvním závodě. Ve 20. století jedno z nejčastějších ženských povolání.' },
  { k: 'učitel autoškoly', re: /autoškol/i, rank: 5, vrstva: 'moderní povolání',
    text: 'Instruktor výuky řízení motorových vozidel – povolání, které se rozšířilo s masovou automobilizací po 2. světové válce.' },
];
export const VRSTVY = ['majitelé gruntů', 'menší usedlíci', 'řemeslníci', 'služebnictvo a námezdní práce', 'bezzemci', 'moderní povolání'];
/** Povolání zmíněná v textu (bez duplicit). */
export const povolaniV = (text) => POVOLANI.filter((x) => x.re.test(text));
/** Fakta, která popisují povolání samotné osoby (ne narození, sňatek, úmrtí ani „syn/dcera …“). */
export const vlastniFakta = (facts = []) => facts.filter((f) => !/^\s*[*×†]/.test(f) && !/^\s*(syn|dcera|z\s)/i.test(f));
