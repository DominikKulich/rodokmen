// Dobové události českých zemí pro kartu osoby „V jaké době žil(a)“.
export const UDALOSTI = [
  [1740, 'Na trůn nastupuje Marie Terezie; začínají války o rakouské dědictví.'],
  [1771, 'Velký hladomor v Čechách – po neúrodě umírají desetitisíce lidí.'],
  [1774, 'Povinná školní docházka (Tereziánská školská reforma).'],
  [1775, 'Selské povstání v Čechách proti robotě.'],
  [1781, 'Josef II. ruší nevolnictví – poddaní se mohou stěhovat a ženit bez svolení vrchnosti.'],
  [1784, 'Matriky se stávají státními knihami s předtištěnými kolonkami.'],
  [1805, 'Bitva u Slavkova.'],
  [1811, 'Státní bankrot – peníze ztrácejí pětinu hodnoty.'],
  [1832, 'První koněspřežka mezi Českými Budějovicemi a Lincem v plném provozu.'],
  [1845, 'První vlak přijíždí do Prahy (dráha Olomouc – Praha).'],
  [1848, 'Zrušení roboty a poddanství – sedláci se stávají svobodnými vlastníky půdy.'],
  [1850, 'Vznikají obce, okresy a okresní hejtmanství v dnešním smyslu.'],
  [1866, 'Prusko-rakouská válka, bitva u Hradce Králové; v zemi řádí cholera.'],
  [1869, 'Říšský školský zákon – osmiletá povinná školní docházka.'],
  [1880, 'Sčítání lidu poprvé zjišťuje i obcovací řeč.'],
  [1891, 'Jubilejní zemská výstava v Praze.'],
  [1914, 'Začíná první světová válka – mobilizace mužů do rakousko-uherské armády.'],
  [1918, 'Vzniká Československo (28. října).'],
  [1919, 'Pozemková reforma – rozdělování velkostatků malým zemědělcům.'],
  [1929, 'Světová hospodářská krize, v Československu nejtvrdší kolem roku 1933.'],
  [1938, 'Mobilizace a Mnichovská dohoda – ztráta pohraničí.'],
  [1939, 'Okupace a Protektorát Čechy a Morava; začíná druhá světová válka.'],
  [1942, 'Heydrichiáda – vyhlazení Lidic nedaleko Slaného.'],
  [1945, 'Konec války a osvobození (květen).'],
  [1948, 'Únorový komunistický převrat.'],
  [1949, 'Začíná kolektivizace – vznikají JZD.'],
  [1953, 'Měnová reforma připravuje lidi o úspory.'],
  [1960, 'Nová ústava, ČSSR; masová výstavba panelových sídlišť.'],
  [1968, 'Pražské jaro a srpnová invaze vojsk Varšavské smlouvy.'],
  [1989, 'Sametová revoluce.'],
  [1993, 'Vzniká samostatná Česká republika.'],
  [2004, 'Česko vstupuje do Evropské unie.'],
];
/** Události v rozmezí života; vrací [{y, t, age}]. */
export function udalostiZivota(by, dy, limit = 6) {
  if (!by) return [];
  const end = dy ?? Math.min(by + 75, 2026);
  const hits = UDALOSTI.filter(([y]) => y >= by && y <= end).map(([y, t]) => ({ y, t, age: y - by }));
  if (hits.length <= limit) return hits;
  // rovnoměrný výběr přes celý život
  return Array.from({ length: limit }, (_, i) => hits[Math.round((i * (hits.length - 1)) / (limit - 1))]);
}
