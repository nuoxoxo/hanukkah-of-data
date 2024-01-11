import pandas as pd

df_order_items = pd.read_csv('./noahs-orders_items.csv')
df_orders = pd.read_csv('./noahs-orders.csv')
df_prod = pd.read_csv('./noahs-products.csv')
df_customers= pd.read_csv('./noahs-customers.csv')

# cat person
cat_prod = df_prod[ df_prod['desc'].str.contains('cat',case=False) ]

# client identity lookup
cat_items = pd.merge(cat_prod, df_order_items, on='sku')
cat_orders = pd.merge(cat_items, df_orders, on='orderid')
cat_clients = pd.merge(cat_orders, df_customers, on='customerid')

# cat person ~ A woman !
res = cat_clients[ cat_clients.citystatezip.str.contains('Staten', case=False) ]\
    .groupby(['name','phone'])\
    .size()\
    .sort_values(ascending=False)\
    .head(4)

print(res, '/res')
