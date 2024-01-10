import os
os.system('python3 2.py && echo "/night 2\n"')

import pandas as pd
df = pd.read_csv('noahs-customers.csv')

# filter cancer people born a rabbit

def is_cancer_of_rabbit(date: str):
    year, month, day = date.split('-')
    if int(year) % 4 == 3 and \
    ((month == '06' and 22<=int(day)<=30) or \
    (month == '07' and 1<=int(day)<=22 )):
        return True
    return False

df = df[df['birthdate'].apply(lambda x: is_cancer_of_rabbit(x))]

# ( 'Jamaica, NY 11435' is a hint returned last night )
# filter 

def is_jamaica( city: str):
    return city.startswith('Jamaica') and city.split()[-1] == '11435'

df = df[df['citystatezip'].apply(lambda x: is_jamaica(x))]

print(df)
print(df[['phone']], '/res')
