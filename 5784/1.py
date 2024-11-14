from utils import gg, yy, cc, rest, nl, yellow, green, cyan
from utils import df_customers as df

head, cols, colslist = df.head(), df.columns, df.columns.tolist()
phone = df['phone']
phone_str_split, phone_no_hyphens = phone.str.split('-'), phone.str.replace('-', '')

print(yellow('head/'), cc, type(head), rest)
print(head)

print(yellow('columns/'), cc, type(cols), rest)
print(cols, nl)
print(yellow('columns/tolist'))
print(', '.join(colslist))
print(yellow('columns/list comprehension from cols'))
print(', '.join(_ for _ in cols))
print(yellow('columns/list comprehension from DF'))
print(', '.join(_ for _ in df), nl)
print(green('observed/\n'), 'same keys when looping a DF or its columns', nl)

print(yellow('phone/'), cc, type(phone), rest)
print(yellow('phone/head'), cc, type(phone.head()), rest)
print(phone, nl)

print(yellow('phone/str/type'), cc, phone.str, rest)
print(yellow('phone/str/'), cc, type(phone.str), rest, nl)
print(yellow('phone/str/split/type'), cc, type(phone_str_split), rest)
print(yellow('phone/str/split'))
print(phone_str_split, nl)

print(yellow('phone/no hyphens'))
print(phone_no_hyphens, nl)

### create new col 'phone2'
df['phone2'] = phone_no_hyphens
print(yellow('added/phone w.o hyphens'))
print(df.head(), nl)

first_and_lastname = df['name'].str.split()
lastname = first_and_lastname.apply(lambda _: _[-1])

print(yellow('1st and last name/type'), cc, type(first_and_lastname), rest)
print(first_and_lastname, nl)
print(yellow('lastname/'))
print(lastname, nl)

def lastname_to_phone(surname) -> str:
    num = ''
    numpad = {'abc':2, 'def':3, 'ghi':4, 'jkl':5, 'mno':6, 'pqrs':7, 'tuv':8, 'wxyz':9}
    for c in surname:
        for k, v in numpad.items():
            if c.lower() in k:
                num += str(v)
                break
    return num

phone_from_lastname = lastname.apply(lastname_to_phone)
df['phone3'] = phone_from_lastname
print(yellow('added/phone from lastnames'))
print(df[['phone', 'phone2', 'phone3']], nl)

res = df[df['phone2'] == df['phone3']]
print(res[['name', 'citystatezip', 'birthdate', 'phone', 'phone3']].to_string(index=False))
print(yellow('res/selected fields'), green('/ends'))
