import pandas as pd

df_orders_items = pd.read_csv('noahs-orders_items.csv')
df_customers = pd.read_csv('noahs-customers.csv')
df_products = pd.read_csv('noahs-products.csv')
df_orders = pd.read_csv('noahs-orders.csv')
[len(_) for _ in [df_orders, df_products, df_orders_items, df_customers]]

# step 1/3 : customers entries w/ JP as initials

def finding_jp (name):
    return ''.join(_[0] for _ in name.split()).upper() == 'JP'
jp = df_customers[df_customers['name'].apply(lambda x: finding_jp (x))]

# step 2/3 - looking for : JP-2017 clients and coffee prod. ref.

#   find who are some of the JP-clients back in '17
orders17 = df_orders[df_orders['ordered'].str.startswith('2017')]
jp17 = pd.merge(orders17, jp, on='customerid')

#   coffee prod. reference - sku - stock keeping unit
coffee_SKU = df_products[df_products['desc'].str.contains('coffee', case=False)]
coffee_orders = pd.merge(coffee_SKU, df_orders_items, on='sku')

# step 3/3 : those JP who ordered coffee back in 2O17

res = pd.merge(coffee_orders, jp17, on='orderid')

print(res[ ['sku', 'desc', 'phone'] ], '/res')
