import pandas as pd

df_order_items = pd.read_csv('./noahs-orders_items.csv')
df_orders = pd.read_csv('./noahs-orders.csv')
df_customers= pd.read_csv('./noahs-customers.csv')

# bakery - BK

bake = df_order_items[ df_order_items['sku'].str.startswith('BK') ]
bakery = df_order_items[ df_order_items['sku'].str.startswith('BKY') ]
assert len(bake) == len(bakery)
bakery_orders = pd.merge(bakery, df_orders, on='orderid', sort=True)
print( len(bakery_orders), '/len all bakery orders')

# early morning bakery orders

def bakery_5am (dt_string):
    _, time = dt_string.split()
    return 0<int(time.split(':')[0])<6

early_morning_bakery_orders = bakery_orders[ bakery_orders['ordered'].apply(lambda x: bakery_5am (x)) ]
print( len(early_morning_bakery_orders), '/len early morning orders')

# name of the best pastry lover

winners_to_sort = pd.merge(early_morning_bakery_orders, df_customers, on='customerid', sort=True)
print( len(winners_to_sort), '/len winners')

res = winners_to_sort.groupby(['name','phone','address']).size().sort_values(ascending=False).head()
print(res, '/res')
