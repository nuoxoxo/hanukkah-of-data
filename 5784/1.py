import pandas as pd
df = pd.read_csv('noahs-customers.csv')

# step 1/3 : get rid of '-' in phone numbers

df['phone_number'] = df['phone'].str.replace('-','')

# step 2/3 : get all the last names

fullnames = df['name'].str.split(expand=True) # Expand split strs into separate cols
midl, last = fullnames[1], fullnames[2]
df['last'] = last.mask( last.isnull(), midl )

# step 3/3 : compare 2 cols - \phone_number and \last

def last_name_to_phone_number (last):
    D={'abc':2,'def':3,'ghi':4,'jkl':5,'mno':6,'pqrs':7,'tuv':8,'wxyz':9}
    res = ''
    for char in last:
        for k,v in D.items():
            if char.lower() in k:
                res += str(v)
                break
    return res

df = df[ ['last','phone_number'] ]
df['smart_number'] = df['last'].apply( last_name_to_phone_number )
res = df[ df['phone_number'] == df['smart_number'] ]

print(res,'/res')
