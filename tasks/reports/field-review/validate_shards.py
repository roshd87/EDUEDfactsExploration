import csv,glob,collections,sys
R='/mnt/c/Repos/EDUEDfacts/'
cols='file_spec_id,file_spec_version,record_kind,organization_level,sequence,field_name,technical_name_or_xml_tag,start_position,length,data_type_or_format,requiredness,definition_text,permitted_values_summary,category_role,source_locator'.split(',')
cat=[(r['file_spec_id'],r['version']) for r in csv.DictReader(open(R+'wiki/reference/edfacts/2026-27/file-specifications/CATALOG-INVENTORY.tsv'),delimiter='\t')]
rows=[]
for f in sorted(glob.glob(R+'tasks/reports/field-review/*-fields.csv')):
    rd=csv.DictReader(open(f,encoding='utf-8'))
    if rd.fieldnames!=cols: print('BAD COLS',f,rd.fieldnames)
    for r in rd: r['_batch']=f.split('/')[-1]; rows.append(r)
k=collections.Counter((r['file_spec_id'],r['file_spec_version'],r['record_kind'],r['organization_level'],r['sequence']) for r in rows)
print('rows',len(rows),'dupkeys',[x for x,c in k.items() if c>1][:10])
hk=collections.Counter((r['file_spec_id'],r['file_spec_version'],r['record_kind']) for r in rows)
present=set((r['file_spec_id'],r['file_spec_version']) for r in rows)
for s in cat:
    if s not in present: continue
    if not hk[s+('header',)] or not hk[s+('data',)]: print('MISSING kind',s,hk[s+('header',)],hk[s+('data',)])
print('covered',len(present&set(cat)),'of',len(cat),'missing',sorted(set(cat)-present))
bad=[r for r in rows if (r['start_position'] and not r['start_position'].isdigit()) or (r['length'] and not r['length'].isdigit())]
print('nonint pos/len',len(bad),[(r['file_spec_id'],r['field_name'],r['start_position'],r['length']) for r in bad[:10]])
print(collections.Counter(r['category_role'] for r in rows))
print(collections.Counter(r['organization_level'] for r in rows))
