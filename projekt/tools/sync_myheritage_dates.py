"""Reconcile all supplied GEDCOM people; preserve evidence and label imported dates.

Uses only the locally supplied export. Does not contact or modify MyHeritage.
"""
from pathlib import Path
from datetime import datetime
import sys,json,re,runpy,shutil,unicodedata
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from ged_import import read,name,events,parents,first,sub,year
DATA=ROOT/'data'; SOURCE=ROOT/'pracovni/audit-myheritage-20261023/myheritage-133-osob.ged'
BASELINE=ROOT/'vystupy/myheritage-2026-10-23/Kulichovi-uplny-rodokmen-2026-10-23.ged'
DATE='23. 10. 2026'
def clean(s):return re.sub(r'\s+',' ',s).strip()
def norm(s):return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower())
def basename(s):return re.sub(r'\s*\([^)]*\d{4}[^)]*\).*','',s).replace(' (Hynek)','').strip()
def signature(date):return tuple(re.findall(r'\d+',date))
def date_of_fact(fact):
 m=re.match(r'^[*†]\s*((?:(?:asi|před|po)\s+)?(?:(?:\d{1,2}\.\s*){1,2})?\d{4})',fact)
 return m[1] if m else ''
def yearpart(text):
 if not text:return ''
 y=year(text)
 if y is None:return ''
 q=next((q for q in ('asi','před','po') if text.strip().startswith(q)), '')
 return ((q+' ') if q else '')+str(y)
def years_label(person):
 b=next((date_of_fact(f) for f in person.get('f',[]) if f.startswith('*') and date_of_fact(f)), '')
 d=next((date_of_fact(f) for f in person.get('f',[]) if f.startswith('†') and date_of_fact(f)), '')
 if not b:
  b=next((re.search(r'\d{4}',f)[0] for f in person.get('f',[]) if f.startswith('*') and re.search(r'\d{4}',f)), '')
 if b and d:return yearpart(b)+'–'+yearpart(d)
 if b:return '* '+yearpart(b)
 if d:return '† '+yearpart(d)
 return person.get('y','')
def dump(name_,obj):(DATA/name_).write_text(json.dumps(obj,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
def main():
 recs=read(SOURCE); old=read(BASELINE)
 inds=[r for r in recs.values() if r['_type']=='INDI']; olds=[r for r in old.values() if r['_type']=='INDI']
 assert len(inds)==133 and all(name(a)==name(b) for a,b in zip(olds,inds))
 mapping={a['_id']:b['_id'] for a,b in zip(olds,inds)}
 ns=runpy.run_path(str(DATA/'osoby.py')); P=ns['P']; SIDE=ns['SIDE']
 shutil.make_archive(str(ROOT/'pracovni'/('pred-uplnym-prenosem-mh-'+datetime.now().strftime('%Y%m%d-%H%M%S'))),'zip',DATA)
 root=next(r for r in inds if name(r)=='Dominik Kulich'); tree={1:root};todo=[1]
 while todo:
  k=todo.pop(0)
  if k>10000:continue
  for kk,p in zip((2*k,2*k+1),parents(tree[k],recs)):
   if p:tree[kk]=p;todo.append(kk)
 matches={}; changed=[]; side_matches={}
 for k,p in P.items():
  if p['st']=='unk':continue
  incoming=mapping.get(f'@I{k}@') or (tree.get(k) or {}).get('_id')
  if incoming:matches[incoming]=k
 for i,s in enumerate(SIDE):
  n=norm(basename(s['n'])); by=year(s['n'])
  candidates=[r for r in inds if norm(name(r))==n and (not by or next((year(d) for t,d,pl,e in events(r,recs) if t=='BIRT'),None)==by)]
  if len(candidates)==1:side_matches[candidates[0]['_id']]=i
 for gid,k in matches.items():
  person=P[k]; supplements=[]
  for typ,d,pl,extra in events(recs[gid],recs):
   if typ not in ('BIRT','DEAT') or not(d or pl):continue
   if k in (1,2,3,5,7) and typ=='BIRT':continue  # living: retain only already-authorized year
   symbol='*' if typ=='BIRT' else '†'
   existing=[f for f in person.get('f',[]) if f.startswith(symbol)]
   if any(signature(d)==signature(date_of_fact(f)) and (not pl or norm(pl) in norm(f)) for f in existing if d):continue
   label=f'{symbol} {d or "datum neuvedeno"}'+(' '+pl if pl else '')
   if existing:
    text='Údaj MyHeritage '+('o narození' if typ=='BIRT' else 'o úmrtí')+': '+label+' (převzato '+DATE+'; původní doklad neověřen)'
   else:text=label+' (MyHeritage, převzato '+DATE+'; původní doklad neověřen)'
   if text not in person['f']:
    person['f'].append(text);supplements.append(text)
  if supplements:
   person['y']=years_label(person)
   person['years_note']='Některé životní údaje jsou převzaté z MyHeritage; u faktů je vyznačeno, které čekají na původní doklad.'
   changed.append(dict(k=k,name=person['n'],years=person['y'],facts=supplements))
  person['myheritage_id']=gid.strip('@').lower()
 for gid,i in side_matches.items():
  s=SIDE[i];parts=[]
  for typ,d,pl,extra in events(recs[gid],recs):
   if typ not in ('BIRT','DEAT') or not(d or pl):continue
   if year(d) and year(d)>=1927 and typ=='BIRT' and not any(t=='DEAT' and dd for t,dd,_,_ in events(recs[gid],recs)):
    d=str(year(d));pl=''
   parts.append(('narození' if typ=='BIRT' else 'úmrtí')+': '+(d or 'datum neuvedeno')+(' '+pl if pl else ''))
  if parts:
   appendix=' Údaje z dodaného exportu MyHeritage ('+DATE+'): '+'; '.join(parts)+'. Převzetí samo nenahrazuje původní doklad; případný rozpor s výše citovanou matrikou se tím neopravuje.'
   if appendix not in s['t']:s['t']+=appendix
  s['myheritage_id']=gid.strip('@').lower()
 src=(DATA/'osoby.py').read_text(encoding='utf-8')
 for k,p in P.items():
  if k not in matches.values():continue
  src,n=re.subn(rf'^ {k}: .*?(?=^ \d+:|^ #|^\}})',lambda m:f' {k}: {p!r},\n',src,count=1,flags=re.M|re.S);assert n==1,k
 begin=src.index('SIDE = [');end=src.index('\n]',begin)+2
 src=src[:begin]+'SIDE = [\n'+''.join(' '+repr(s)+',\n' for s in SIDE)+']'+src[end:]
 (DATA/'osoby.py').write_text(src,encoding='utf-8')
 inventory=[];eventcount=0
 for ind in inds:
  gid=ind['_id'];ev=events(ind,recs)
  death=any(t=='DEAT' and d for t,d,pl,e in ev) or first(ind,'DEAT')=='Y'
  born=next((year(d) for t,d,pl,e in ev if t=='BIRT'),None)
  living=not death and (born is None or born>=1927)
  public_events=[]
  for typ,d,pl,extra in ev:
   if not(d or pl):continue
   if living:
    d=str(year(d)) if year(d) else '';pl=''
   if not(d or pl):continue
   public_events.append(dict(type=typ,date=d,place=pl))
  eventcount+=len(public_events)
  father,mother=parents(ind,recs)
  spouses=[];children=[]
  for f in sub(ind,'FAMS'):
   fam=recs.get(f['val'])
   if not fam:continue
   spouses += [n['val'].strip('@').lower() for n in fam['_sub'] if n['tag'] in ('HUSB','WIFE') and n['val']!=gid]
   children += [n['val'].strip('@').lower() for n in fam['_sub'] if n['tag']=='CHIL']
  inventory.append(dict(id=gid.strip('@').lower(),name=name(ind),events=public_events,
   canonicalK=matches.get(gid),sideK=SIDE[side_matches[gid]]['k'] if gid in side_matches else None,
   father=father['_id'].strip('@').lower() if father else None,mother=mother['_id'].strip('@').lower() if mother else None,
   spouses=list(dict.fromkeys(spouses)),children=list(dict.fromkeys(children)),
   mediaCount=len(sub(ind,'OBJE')),privacy='Žijící nebo nejisté: jen roky, bez přesných míst.' if living else '',
   status='Údaje exportu; shoda s kartou sama neznamená matriční ověření.'))
 result=dict(date=DATE,source='Dodaný GEDCOM export MyHeritage, 133 osob; nejde o živou synchronizaci účtu.',
  count=len(inventory),families=sum(r['_type']=='FAM' for r in recs.values()),events=eventcount,
  canonicalMatched=len(matches),sideMatched=len(side_matches),changed=changed,people=inventory,
  scope='Úplný soupis osob, událostí a rodinných vazeb z tohoto souboru. Kontakty a surové poznámky se nezveřejňují. Fotografie mají samostatné doklady a nejsou tímto počtem potvrzené jako všechny přenesené.')
 dump('myheritage_import.json',result)
 assert len({p['id'] for p in inventory})==133
 assert all(p['id'] for p in inventory)
 report=['# Úplné porovnání dat z dodaného MyHeritage exportu','',result['source'],'',
  f'Zkontrolováno {len(inventory)} osob, {result["families"]} rodin, {eventcount} veřejně zobrazitelných událostí. Přímých předků přiřazeno {len(matches)}, bočních osob {len(side_matches)}.','',
  'Všech 133 osob je v přehledu MyHeritage na webu, včetně vazeb. Karty předků a bočních osob mají navázané odpovídající položky. Nepotvrzená data jsou výslovně označena; známé matriční rozpory se nepřepisují. Žijící lidé pouze rokem, bez přesného místa. Fotografie a surové poznámky nejsou součástí tohoto automatického přenosu dat.','',
  '## Doplněné údaje přímých předků','']
 for c in changed:
  report+=['### '+c['name']+' · '+c['years']]+['- '+f for f in c['facts']]+['']
 report+=['## Úplný kontrolní soupis','']
 for p in inventory:
  report += [f'- {p["id"]}: {p["name"]} — '+'; '.join(e['type']+' '+e['date']+' '+e['place'] for e in p['events'])]
 (ROOT/'KONTROLA_PRENOSU_MYHERITAGE_2026-10-23.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
 print('Zkontrolováno',len(inventory),'osob;',eventcount,'událostí;',len(changed),'předků s doplněními.')
 for c in changed:print(c['k'],c['name'],c['years'])
if __name__=='__main__':main()
