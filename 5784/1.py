import pandas as pd
NC = pd.read_csv('noahs-customers.csv')
print(NC)
print(NC.head())

phone2 = NC['phone'].str.replace('-','')
NC['phone2'] = phone2
phone2_idx = NC.columns.get_loc("phone2")
phone_idx = NC.columns.get_loc("phone")
cols = NC.columns.tolist()
cols = cols[:phone_idx + 1] + cols[phone2_idx:phone2_idx + 1] + cols[phone_idx + 1:phone2_idx]
NC = NC[cols]

fullnames = NC['name'].str.split(expand=True) # Expand split strs into separate cols
midl, last = fullnames[1], fullnames[2]
last = last.mask( last.isnull(), midl )
NC['last'] = last
name_idx = NC.columns.get_loc("name")
last_idx = NC.columns.get_loc("last")
cols = NC.columns.tolist()
cols = cols[:name_idx + 1] + cols[last_idx:last_idx + 1] + cols[name_idx + 1:last_idx]
NC = NC[cols]

NC = NC[['last','phone2']]

def last_name_to_phone_number (last):
    D={'abc':2,'def':3,'ghi':4,'jkl':5,'mno':6,'pqrs':7,'tuv':8,'wxyz':9}
    res = ''
    for char in last:
        for k,v in D.items():
            if char.lower() in k:
                res += str(v)
                break
    return res

NC['to_check'] = NC['last'].apply( last_name_to_phone_number )

res = NC[ NC['phone2'] == NC['to_check'] ]
print(res,'/res')
