import csv,glob,re,collections,sys
R='/mnt/c/Repos/EDUEDfacts/'
FAM={'b1-idea':'IDEA Part B/C + dispute resolution','b2-directory-org':'Directory, org & accountability','b3-student-staff':'Student counts & staff','b4-assessment-el':'Assessment & EL','b5-program':'Program participation'}
def norm(n):
    n=n.replace('–','-').replace('—','-').replace(' ',' ').replace('\n',' ')
    n=re.sub(r'^(revised!|new!)\s*','',n.strip(),flags=re.I)
    n=re.sub(r'^DG\s*\d+(?:[NP](?=[A-Z ]))?\s*','',n)
    n=re.sub(r'\s+',' ',n).strip().lower()
    n=re.sub(r'(\w)\(',r'\1 (',n).replace('(sate)','(state)')
    if n.count('(')>n.count(')'): n+=')'
    n=re.sub(r'\s*-\s*(sea|lea|school|la)$','',n)
    n=re.sub(r'^racial ?/ ?ethnic$','racial ethnic',n)
    if n.startswith('carriage return'): n='carriage return / line feed (crlf) or line feed (lf)'
    n=n.replace('leasy start','lea sy start')
    if n=='teachers fte': n='teacher fte'
    return n
def ndef(t): return re.sub(r'\s+',' ',t).strip()
def edef(t):
    t=ndef(t).lower().replace('’',"'").replace('“','"').replace('”','"').replace('–','-').replace('—','-')
    return re.sub(r'[^a-z0-9]+','',t)
def pv(s):
    s=re.sub(r'^category:[^=]*=','',s.strip())
    return s
def codes(s):
    s=pv(s).replace('[','').replace(']','').replace('\u2013','-').replace('\u2014','-').lower()
    out=set()
    for c in re.split(r';| or ',s):
        c=re.sub(r'\s+',' ',c).strip(' .')
        c=re.sub(r'\s*-\s*',' - ',c) if 'level' in c else c
        if c and c!='or' and not re.match(r'(for a list|see |refer|this will|sea level|lea level|two-character|\(see|\[see)',c) and 'level - blank' not in c: out.add(c)
    return frozenset(out)
import difflib
def simil(a,b):
    a,b=edef(a),edef(b)
    if a in b or b in a: return 1.0
    return difflib.SequenceMatcher(None,a,b).ratio()
BYDESIGN={'file type':'values: file-specific by design (each spec prints its own SEA/LEA/SCHOOL file-type literals)','table name':'values: file-specific by design (each spec prints its own technical table names)'}
rows=[]
for f in sorted(glob.glob(R+'tasks/reports/field-review/*-fields.csv')):
    b=f.split('/')[-1].split('-fields')[0]
    for r in csv.DictReader(open(f,encoding='utf-8')):
        r['_fam']=FAM[b]; r['_n']=norm(r['field_name'])
        if r['_n'] in('filler','carriage return / line feed (crlf) or line feed (lf)'): r['_n']+=' ['+r['record_kind']+']'
        rows.append(r)
g=collections.defaultdict(list)
for r in rows: g[r['_n']].append(r)
def mode(vals): return collections.Counter(vals).most_common(1)[0][0]
def deviants(rs,key,m):
    d=sorted(set(r['file_spec_id']+('' if r['organization_level']=='all' else '/'+r['organization_level'])+('' if r['file_spec_version']=='v23.0' else '@'+r['file_spec_version']) for r in rs if key(r)!=m))
    return d
out=[]
for n,rs in g.items():
    specs=sorted(set(r['file_spec_id'] for r in rs))
    if len(specs)<2: continue
    fams=set(r['_fam'] for r in rs)
    var=[]
    pm=mode([r['start_position'] for r in rs]); lm=mode([r['length'] for r in rs])
    pc='yes' if len(set(r['start_position'] for r in rs))==1 else 'no'
    lc='yes' if len(set(r['length'] for r in rs))==1 else 'no'
    if n.startswith('filler'): pc='n/a'
    if pc=='no':
        dv=deviants(rs,lambda r:r['start_position'],pm); var.append(f"position {pm} in most; differs in {len(dv)}: "+','.join(dv[:12])+('…' if len(dv)>12 else '')+f" (distinct starts: {';'.join(sorted(set(r['start_position'] for r in rs),key=int))})")
    if lc=='no':
        dv=deviants(rs,lambda r:r['length'],lm); var.append(f"length {lm} in most; differs: "+';'.join(sorted(set(f"{r['file_spec_id']}={r['length']}" for r in rs if r['length']!=lm)))[:400])
    defs=[ndef(r['definition_text']) for r in rs]
    if len(set(defs))==1: di='identical'
    else:
        cd0=mode(defs)
        di='equivalent' if min(simil(d,cd0) for d in set(defs))>=0.85 else 'differs'
    cd=mode(defs)
    if di!='identical':
        dv=deviants(rs,lambda r:ndef(r['definition_text']),cd)
        var.append(f"definition: {len(set(defs))} wordings; non-canonical in "+','.join(dv[:12])+('…' if len(dv)>12 else ''))
    pvs=[pv(r['permitted_values_summary']) for r in rs]
    if all(not p for p in pvs): pi='n/a'
    elif len(set(pvs))==1: pi='identical'
    elif n in BYDESIGN: pi='differs'
    elif len(set(codes(p) for p in pvs))==1: pi='equivalent'
    else: pi='differs'
    if n in BYDESIGN: var.append(BYDESIGN[n])
    elif pi=='differs':
        pmv=mode([codes(p) for p in pvs])
        alt={}
        for r in rs:
            c=codes(r['permitted_values_summary'])
            if c!=pmv:
                d=('+'+'+'.join(sorted(c-pmv)) if c-pmv else '')+(' -'+' -'.join(sorted(pmv-c)) if pmv-c else '')
                alt.setdefault(d.strip(),set()).add(r['file_spec_id'])
        var.append(f"values: most use {';'.join(sorted(pmv))[:120] or '(blank)'}; differ: "+' | '.join(f"{','.join(sorted(v))}: {k}" for k,v in sorted(alt.items()))[:500])
    ty=collections.Counter(r['data_type_or_format'].strip() for r in rs)
    if len(ty)>1: var.append('type varies: '+'; '.join(f"{k or '(blank)'} x{v}" for k,v in ty.most_common()))
    req=set(r['requiredness'] for r in rs)
    if len(req)>1: var.append('requiredness varies: '+'/'.join(sorted(req)))
    nfam=len(fams)
    rc='universal' if (nfam>=4 and len(specs)>=20) else ('family-wide' if len(specs)>=4 else 'collection-specific')
    out.append(dict(field_name_normalized=n,specs_count=len(specs),specs=';'.join(specs),record_kinds=';'.join(sorted(set(r['record_kind'] for r in rs))),
      position_consistent=pc,length_consistent=lc,definition_identical=di,permitted_values_identical=pi,canonical_definition=cd,
      variants=' || '.join(var),reuse_class=rc,_fam=';'.join(sorted(fams)),_pos=pm,_len=lm,_role=mode([r['category_role'] for r in rs])))
OV={
'state code':('equivalent','manual: FS045 says "Federal Information Processing Standards" instead of ANSI (same 2-digit codes); FS029 prefixes "See section 2.3.1"; FS006/FS170 omit "code"; FS151 typo "ASNI"; FS029 points to Appendix A instead of the EDFacts Workbook'),
'lea identifier (state)':('equivalent','manual: FS175/178/179/185/188/189 add "This ID is a required field"; FS029 abbreviates and omits "cannot be updated through this file"; most specs note "SEA level - Blank" in the values cell'),
'school identifier (state)':('equivalent','manual: assessment/accountability specs drop "(SEA)"; FS132/150/151/163/165 typo "States"; FS029 abbreviates; starts at 36 in FS029 School, FS039 and FS197 because LEA Identifier (NCES) occupies 29-35'),
'filler [data]':('equivalent','manual: every wording is "leave filler blank"; length is whatever the slot needs (7-125), Pop is M, A or blank'),
'table name':('equivalent','manual: every wording points to the spec\'s own technical-name table; FS193 starts at 29 (no LEA/School IDs before it) and FS099 at 44'),
'total indicator':('equivalent','manual: wording differs only in which totals table it cites; values differ for real - N only (no subtotals) in the specs listed'),
'state agency number':(None,'same DG570 slot as "Lead Agency Number" (pos 13, len 2): value 01 here, 02 in FS029 v23.1 and FS901-908'),
'lead agency number':(None,'same DG570 slot as "State Agency Number" (pos 13, len 2) with value 02; FS906-908 define it as "state agencies", FS901-905 and FS029 v23.1 as "lead agencies"'),
'due process complaint result':(None,'FS908 prints FS229\'s Resolution Meeting Outcome definition here (definitions swapped); codes and positions agree'),
'resolution meeting outcome':(None,'FS908 prints FS229\'s Due Process Complaint Result definition here (definitions swapped); codes and positions agree'),
'racial ethnic':(None,'value order differs only by extraction source; all 24 use AM7;AS7;BL7;HI7;PI7;WH7;MU7;MISSING'),
'disability category (idea)':(None,'FS006 and FS089 add "Individualized Family Service Plan (IFSP)" to the definition'),
'state defined status indicator':(None,'each spec names its own status field (Graduation Rate / Academic Achievement / Academic Progress / SQSS / ELP)'),
'military connected student status':(None,'length 125 in FS175/178/179 (achievement) vs 15 in FS185/188/189 (participation), as printed'),
'teacher fte':('equivalent','manual: both wordings permit decimals to one hundredth FTE; starts at 330 in FS059/FS070, 145 in FS203; FS059 prints the name as "Teachers FTE"'),
'staff fte':('equivalent','manual: both wordings permit decimals to one hundredth FTE; FS099 starts at 345 vs 330 in FS059'),
'student count':(None,'definition cell is empty in every spec; FS151 prints length 8'),
'carriage return / line feed (crlf) or line feed (lf) [header]':(None,'header record length differs from the data record length in 57 of 94 spec-versions; header Filler is not padding to the data length'),
'filler [header]':(None,'always starts at 127; length = header record length - 127, varies 143-753'),
}
for o in out:
    v=OV.get(o['field_name_normalized'])
    if v:
        if v[0]: o['definition_identical']=v[0]
        o['variants']=(v[1]+(' || '+o['variants'] if o['variants'] else ''))
out.sort(key=lambda x:(-x['specs_count'],x['field_name_normalized']))
cols='field_name_normalized,specs_count,specs,record_kinds,position_consistent,length_consistent,definition_identical,permitted_values_identical,canonical_definition,variants,reuse_class'.split(',')
with open(R+'wiki/analysis/edfacts-2026-27-shared-fields.csv','w',newline='',encoding='utf-8') as fh:
    w=csv.DictWriter(fh,fieldnames=cols,extrasaction='ignore',lineterminator='\n'); w.writeheader(); w.writerows(out)
import json; json.dump(out,open(sys.argv[1],'w')) if len(sys.argv)>1 else None
print('distinct normalized fields',len(g),'shared',len(out))
print(collections.Counter(o['reuse_class'] for o in out))
print('def',collections.Counter(o['definition_identical'] for o in out),'pv',collections.Counter(o['permitted_values_identical'] for o in out))
print('pos',collections.Counter(o['position_consistent'] for o in out),'len',collections.Counter(o['length_consistent'] for o in out))
full=[o for o in out if o['definition_identical']=='identical' and o['permitted_values_identical'] in('identical','n/a') and o['length_consistent']=='yes' and o['position_consistent'] in('yes','n/a')]
print('fully identical',len(full))
for o in out:
    if o['reuse_class']!='collection-specific': print(o['specs_count'],o['reuse_class'][:4],o['field_name_normalized'],o['_pos'],o['_len'],o['position_consistent'],o['length_consistent'],o['definition_identical'],o['permitted_values_identical'],'|',o['_fam'])
