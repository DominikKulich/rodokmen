"""Export aktuálního doloženého rodokmenu do GEDCOM 5.5.1 pro MyHeritage.

Původní data nemění. Nejistoty zachovává v poznámkách, neznámé rodiče
nevytváří. Boční vztahy níže jsou výslovně popsány v data/osoby.py.
"""
from pathlib import Path
import json
import re
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
OUT = ROOT / 'vystupy' / 'myheritage-2026-10-23'
BASE = 'https://rodokmen.dominikkulich.cz'
MONTHS = 'JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC'.split()
STATUS = {'doc': 'Doloženo původním zápisem; jednotlivé nejistoty viz poznámky.',
          'fam': 'Údaj od rodiny, nikoli samostatně ověřený matriční doklad.',
          'prob': 'Pravděpodobné / nejisté údaje, nutno ověřit.', 'unk': 'Neověřeno.'}


def load(name):
    return json.loads((DATA / name).read_text(encoding='utf-8'))


def date_and_rest(text):
    text = text.strip().lstrip('*×† ').strip()
    qualifier = ''
    for prefix, ged in [('asi ', 'ABT '), ('před ', 'BEF '), ('po ', 'AFT ')]:
        if text.startswith(prefix):
            qualifier, text = ged, text[len(prefix):]
            break
    m = re.match(r'(\d{1,2})\.\s*(\d{1,2})\.\s*(\d{4})(.*)', text)
    if m:
        d, mo, y, rest = m.groups()
        return f'{qualifier}{int(d)} {MONTHS[int(mo)-1]} {y}', rest.strip()
    m = re.match(r'(\d{4})(.*)', text)
    return (qualifier + m[1], m[2].strip()) if m else ('', text)


def main():
    ns = runpy.run_path(str(DATA / 'osoby.py'))
    people, families = {}, {}
    sources = {r['klic']: r for r in load('zaznamy.json')}
    volumes, transcripts = load('svazky.json'), load('prepisy.json')
    source_ids = {key: f'S{i+1}' for i, key in enumerate(sources)}
    for k, p in sorted(ns['P'].items()):
        if p['n'].startswith(('otec neuveden', 'matka neuvedena')):
            continue
        people[f'I{k}'] = dict(name=p['n'], sex=p.get('sex', 'M' if k % 2 == 0 or k == 1 else 'F'),
                              facts=p.get('f', []), note=p.get('note', ''), years=p.get('y', ''),
                              records=p.get('r', []), status=p.get('st', 'unk'), events=[])
    for i, s in enumerate(ns['SIDE']):
        name = re.sub(r'\s*\([^)]*\d{4}[^)]*\).*', '', s['n']).strip()
        nickname = 'Hynek' if '(Hynek)' in name else None
        name = name.replace(' (Hynek)', '')
        sex = 'F' if 'Sestra' in s['t'] or s['n'].startswith(('Marie Trnková', 'Marcela ')) else 'M'
        years = re.search(r'\(([^)]*\d{4}[^)]*)\)', s['n'])
        people[f'B{i}'] = dict(name=name, sex=sex, nickname=nickname, facts=[],
                              note=s['t'], years=years[1] if years else '', records=s.get('r', []),
                              status='doc' if s.get('r') else 'fam', events=[])

    def add_person(id, name, sex, facts=(), records=(), status='doc', note=''):
        people[id] = dict(name=name, sex=sex, facts=list(facts), records=list(records),
                          status=status, note=note, years='', events=[])

    def family(father, mother, children=(), marriage=None, records=()):
        key = (father, mother)
        if key not in families:
            families[key] = dict(id=f'F{len(families)+1}', father=father, mother=mother,
                                 children=[], marriage=marriage, records=list(records))
        f = families[key]
        f['children'] = list(dict.fromkeys(f['children'] + list(children)))
        if marriage:
            f['marriage'] = marriage
        f['records'] = list(dict.fromkeys(f['records'] + list(records)))
        return f

    for k, p in sorted(ns['P'].items()):
        if f'I{k}' not in people:
            continue
        father = f'I{2*k}' if f'I{2*k}' in people else None
        mother = f'I{2*k+1}' if f'I{2*k+1}' in people else None
        if not (father or mother):
            continue
        marriage = None
        if father and mother:
            spouse = people[mother]['name'].split()[0]
            marriage = next((x for x in people[father]['facts'] if x.startswith('×') and spouse in x), None)
            if marriage:
                marriage = marriage.split(spouse)[0].strip()
        family(father, mother, [f'I{k}'], marriage)
        links = [ns['P'].get(2*k, {}).get('parent_link'), ns['P'].get(2*k+1, {}).get('parent_link')]
        if 'fam' in links:
            people[f'I{k}']['note'] += '\nVazba k rodičům je potvrzeným údajem od rodiny (Dominik, 22. 10. 2026); rodný list není dosud získán.'

    # Sourozenci mají rodiče stejné jako předek, ke kterému jsou přiřazeni.
    for i, s in enumerate(ns['SIDE']):
        if not re.match(r'(?:Nejstarší bratr|Bratr |Sestra )', s['t']):
            continue
        k = s['k']
        father = f'I{2*k}' if f'I{2*k}' in people else None
        mother = f'I{2*k+1}' if f'I{2*k+1}' in people else None
        family(father, mother, [f'B{i}'])
    family('B3', 'B1', ['B2'], '17. 10. 1887 Konice', ['cunin_snatek_frantisek_polak_marie_trnkova_1887'])
    add_person('E1', 'Filomena Hrušáková (?)', 'F', records=['cunin_krest_jan_polak_1893_eduard'],
               status='prob', note='Matka Jana narozeného 16. 4. 1893; rodné příjmení čteno nejistě. Sňatek s Eduardem Polákem 19. 5. 1891 uveden v poznámkách výzkumu.')
    family('B4', 'E1', ['B0'], '19. 5. 1891 Konice', ['cunin_krest_jan_polak_1893_eduard'])
    add_person('E2', 'Josef Trnka', 'M', ['domkář v Čuníně'], ['cunin_snatek_frantisek_polak_marie_trnkova_1887'])
    add_person('E3', 'Anna', 'F', records=['cunin_snatek_frantisek_polak_marie_trnkova_1887'], note='Matka Marie Trnkové; rodné příjmení není ověřeno.')
    family('E2', 'E3', ['B1'])
    add_person('E4', 'Helena Kmentová', 'F', ['* 10. 2. 1895'], ['premyslovice_snatek_jan_polak_helena_kmentova_1915'])
    family('B9', 'E4', marriage='31. 8. 1915 Přemyslovice', records=['premyslovice_snatek_jan_polak_helena_kmentova_1915'])
    # Další partneři jsou doloženi/čteni v přípiscích, nejistá jména zůstávají označena.
    extra_spouses = [
        ('E5', 'Albína Šmerdová (?)', 'F', 'I28', '5. 7. 1923 Rozsochy', 'domanin_krest_ignac_kastanek_1878'),
        ('E6', 'Růžena Vaší…ová (?)', 'F', 'I28', '16. 10. 1934 Rozsochy', 'domanin_krest_ignac_kastanek_1878'),
        ('E7', 'Methoděj Veselý (?)', 'M', 'B10', '1. 10. 1917 Konice', 'cunin_krest_vincencie_polakova_1894'),
        ('E8', 'Bedřich Kupla (?)', 'M', 'B11', '29. 8. 1921 Konice', 'cunin_krest_ruzena_polakova_1896'),
        ('E9', 'Anna Hýblová', 'F', 'B18', '18. 10. 1941 Konice', 'cunin_krest_antonin_polak_1914'),
        ('E10', 'Marie Pl…ová (?)', 'F', 'B23', '22. 9. 1935', 'rozinka_krest_ignac_kastanek_1910'),
        ('E11', 'Helena Vítková (?)', 'F', 'B24', '24. 10. 1935', 'rozinka_krest_hubert_kastanek_1912'),
        ('E12', 'Štěpánka Škudová (?)', 'F', 'B25', '24. 9. 1939 Bystřice', 'rozinka_krest_josef_kastanek_1919')]
    for id, name, sex, partner, marriage, source in extra_spouses:
        add_person(id, name, sex, records=[source], status='prob' if '(?)' in name else 'doc',
                   note='Partner/partnerka uvedený/á v přípisku. Nejisté čtení příjmení zachováno podle výzkumu.')
        family(partner if sex == 'F' else id, id if sex == 'F' else partner, marriage=marriage, records=[source])

    # Přesné události bočních osob čerpají z jejich výslovného popisu.
    side_birth = {
        0: '16. 4. 1893 Čunín čp. 71', 1: 'asi 1862', 2: '4. 7. 1890 Čunín čp. 13',
        3: '18. 10. 1860 Čunín čp. 64', 4: '16. 11. 1868 Čunín čp. 64',
        5: '19. 3. 1872 Čunín čp. 25', 6: '24. 12. 1873 Čunín čp. 25',
        7: '6. 4. 1876 Čunín čp. 25', 8: '13. 12. 1878 Čunín čp. 25',
        9: '17. 1. 1893 Čunín čp. 25', 10: '1894 Čunín čp. 26', 11: '18. 12. 1896 Čunín čp. 26',
        12: '12. 1. 1899 Čunín čp. 26', 13: 'JUL 1900', 14: '4. 10. 1901 Čunín čp. 26',
        15: 'JAN 1904', 16: '9. 3. 1908 Čunín čp. 26', 17: '10. 3. 1912 Čunín čp. 26',
        18: '26. 2. 1914 Čunín čp. 26', 21: '7. 10. 1905 Dolní Rožínka čp. 26',
        22: '28. 6. 1908 Dolní Rožínka čp. 26', 23: '25. 2. 1910 Zámecká Rožínka čp. 26',
        24: '28. 10. 1912 Dolní Rožínka čp. 26', 25: '3. 3. 1919 Dolní Rožínka'}
    for i, birth in side_birth.items():
        if birth.startswith(('JAN ', 'JUL ')):
            people[f'B{i}']['events'].append(('BIRT', birth, 'Čunín čp. 26', 'Datum narození uvedeno pouze měsícem a rokem.'))
        else:
            people[f'B{i}']['facts'].append('* ' + birth)
    for i, death in {4:'25. 7. 1923',5:'1872',6:'DEC 1873',7:'6. 4. 1876',8:'13. 12. 1878',
                     12:'13. 2. 1899',13:'23. 10. 1900',14:'14. 1. 1959 Senice na Hané',
                     15:'19. 2. 1905',16:'28. 1. 1912',22:'1909'}.items():
        if death.startswith('DEC '):
            people[f'B{i}']['events'].append(('DEAT', death, '', 'Přípisek v křestním zápisu.'))
        else:
            people[f'B{i}']['facts'].append('† ' + death)
    people['B2']['facts'].append('krejčí, domovsky Prostějov')
    people['B2']['note'] += '\nOsobní účast u Zborova a na Transsibiřské magistrále dosud není doložena. Historie pluku není dokladem osobní účasti.'
    for tag, date, place, note in [('EVEN','2 MAR 1915','Karpaty','Zajetí; rakousko-uherský 93. pěší pluk.'),
                                   ('EVEN','24 MAY 1917','Rusko','Nástup k 1. československému střeleckému pluku ruských legií.'),
                                   ('EVEN','8 JUL 1920','','Demobilizace z legií; hodnost vojín.')]:
        people['B2']['events'].append((tag, date, place, note))

    lines = []
    def line(level, tag, value=''):
        lines.append(f'{level} {tag}' + (f' {value}' if value else ''))
    def text(level, tag, value):
        chunks = str(value).replace('\r','').split('\n')
        for n, paragraph in enumerate(chunks):
            # GEDCOM maximum line length is 255 bytes including prefix and terminator.
            chunks_utf8, chunk = [], ''
            for char in paragraph:
                if len((chunk + char).encode('utf-8')) > 220:
                    chunks_utf8.append(chunk); chunk = ''
                chunk += char
            chunks_utf8.append(chunk)
            for j, chunk in enumerate(chunks_utf8):
                line(level if n == j == 0 else level+1, tag if n == j == 0 else ('CONT' if j == 0 else 'CONC'), chunk)
    def citation(level, key):
        if key in source_ids:
            line(level, 'SOUR', f'@{source_ids[key]}@')
            line(level+1, 'PAGE', f"{sources[key].get('datum','')}; snímek {sources[key].get('snimek','')}")
    def event(tag, date, place='', note='', records=()):
        line(1, tag)
        if tag == 'EVEN': line(2, 'TYPE', note.split(';')[0])
        if date: line(2, 'DATE', date)
        if place: text(2, 'PLAC', place)
        if note: text(2, 'NOTE', note)
        for key in records: citation(2, key)

    line(0, 'HEAD');line(1,'SOUR','RODOKMEN_KULICH');line(2,'NAME','Rodokmen Kulichových – doložené rodinné bádání')
    line(1,'DEST','MyHeritage');line(1,'DATE','23 OCT 2026');line(1,'SUBM','@SUB1@')
    line(1,'GEDC');line(2,'VERS','5.5.1');line(2,'FORM','LINEAGE-LINKED');line(1,'CHAR','UTF-8');line(1,'LANG','Czech')
    line(0,'@SUB1@ SUBM');line(1,'NAME','Dominik Kulich')
    text(1,'NOTE','Export rodokmenu ze dne 23. 10. 2026. Rodinné údaje a nejistá čtení jsou výslovně označeny. Původní doklady, přepisy a fotografie: '+BASE)
    for id,p in people.items():
        line(0, f'@{id}@ INDI')
        cleaned=p['name'].replace(' (?)','').strip();parts=cleaned.rsplit(' ',1)
        given,surname=parts if len(parts)==2 else (cleaned,'')
        if '(?)' in p['name']: surname+=' (?)'
        line(1,'NAME',f'{given} /{surname}/');line(2,'GIVN',given)
        if surname:line(2,'SURN',surname)
        if p.get('nickname'):line(2,'NICK',p['nickname'])
        line(1,'SEX',p['sex'])
        used=set()
        for fact in p['facts']:
            if fact.startswith(('*','†')):
                tag='BIRT' if fact.startswith('*') else 'DEAT'
                dtext=fact.lstrip('*† ').strip()
                if dtext.startswith('(křest)'):
                    tag='CHR';dtext=dtext[len('(křest)'):].strip()
                d,rest=date_and_rest(dtext)
                if d:
                    place=rest if rest and '?' not in rest and not rest.startswith('(') else ''
                    event(tag,d,place,fact,p['records']);used.add(tag)
        if 'BIRT' not in used and not any(e[0]=='BIRT' for e in p['events']):
            y=p['years'].split('–')[0].strip()
            d,_=date_and_rest(y)
            if d:event('BIRT',d,note='Rok narození podle souhrnu; míra jistoty viz poznámka.',records=p['records'])
        for e in p['events']:event(*e,records=p['records'])
        if 'Žijící' in p['note']:line(1,'_LIVING','Y')
        text(1,'NOTE',STATUS[p['status']]+'\n'+p['note']+'\n'+'\n'.join(p['facts']))
        if id=='I1':
            text(1,'NOTE','Rodinné zajímavosti:\n'+(DATA/'zajimavosti.md').read_text(encoding='utf-8'))
            text(1,'NOTE','Otevřené a vyřešené otázky:\n'+'\n'.join(q+' '+a for q,a in ns['ISSUES']))
            line(1,'WWW',BASE)
        for f in families.values():
            if id in f['children']:line(1,'FAMC',f"@{f['id']}@")
            if id in (f['father'],f['mother']):line(1,'FAMS',f"@{f['id']}@")
        for key in p['records']:citation(1,key)
        if id=='B2':
            line(1,'OBJE','@MPHOTO@');line(1,'WWW',BASE+'/legionar/')
        for key in p['records']:
            if (ROOT/'vyrezy'/f'{key}.jpg').exists():line(1,'OBJE',f'@M{source_ids[key]}@')
    for f in families.values():
        line(0,f"@{f['id']}@ FAM")
        if f['father']:line(1,'HUSB',f"@{f['father']}@")
        if f['mother']:line(1,'WIFE',f"@{f['mother']}@")
        for child in f['children']:line(1,'CHIL',f'@{child}@')
        if f['marriage']:
            d,place=date_and_rest(f['marriage']);event('MARR',d,place,records=f['records'])
        for key in f['records']:citation(1,key)
    for key,s in sources.items():
        sv=volumes.get(s.get('svazek'),{});tr=transcripts.get(key,{})
        line(0,f'@{source_ids[key]}@ SOUR');text(1,'TITL',s.get('nazev',key));text(1,'AUTH',sv.get('archiv','Původní pramen'))
        text(1,'PUBL',sv.get('svazek','')+'; '+s.get('datum','')+f"; snímek {s.get('snimek','')}")
        text(1,'TEXT',s.get('shrnuti',''))
        text(1,'NOTE','Archivní odkaz: '+(s.get('odkaz') or sv.get('url',''))+'\nDoklad a výřez: '+BASE+'/zdroj/'+key+'/')
        if tr:text(1,'TEXT','Přepis originálu:\n'+tr.get('orig','')+'\nČeský překlad:\n'+tr.get('cs',''))
        if 'neprirazeno' in key:text(1,'NOTE','NEPŘIŘAZENO: totožnost s někým z rodiny dosud není doložena. Pramen se necituje jako úmrtí žádné rodinné osoby.')
        if (ROOT/'vyrezy'/f'{key}.jpg').exists():line(1,'OBJE',f'@M{source_ids[key]}@')
    media=[]
    for key,s in sources.items():
        if not (ROOT/'vyrezy'/f'{key}.jpg').exists():continue
        line(0,f'@M{source_ids[key]}@ OBJE');line(1,'FILE',BASE+'/img/'+key+'.jpg');line(2,'FORM','jpg');text(2,'TITL',s.get('nazev',key))
        media.append(str(ROOT/'vyrezy'/f'{key}.jpg'))
    line(0,'@MPHOTO@ OBJE');line(1,'FILE',BASE+'/img/frantisek-polak-legionar-foto-2.jpg');line(2,'FORM','jpg');line(2,'TITL','František Polák (1890), legionář – archivní fotografie ČsOL')
    line(1,'NOTE','Původní fotografie ČsOL, včetně zachovaného označení původu.')
    media.append(str(ROOT/'web/public/img/frantisek-polak-legionar-foto-2.jpg'))
    line(0,'TRLR')
    OUT.mkdir(parents=True,exist_ok=True)
    path=OUT/'Kulichovi-uplny-rodokmen-2026-10-23.ged'
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (OUT/'media.json').write_text(json.dumps(media,ensure_ascii=False,indent=2),encoding='utf-8')
    report={'people':len(people),'families':len(families),'sources':len(sources),'media':len(media),
            'people_index':{id:p['name'] for id,p in people.items()},'tree_name':'Kulichovi – úplný rodokmen 2026'}
    (OUT/'export.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    assert all(len(x.encode('utf-8'))<=253 for x in lines),'Příliš dlouhý řádek GEDCOM'
    assert not any(f['father'] is None and f['mother'] is None for f in families.values())
    print(json.dumps({**{k:v for k,v in report.items() if k!='people_index'},'file':str(path)},ensure_ascii=False))


if __name__=='__main__':main()
