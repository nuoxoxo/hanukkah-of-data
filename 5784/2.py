from utils import gg, yy, cc, rest, nl, yellow, green, cyan
from utils import pd, df_customers, df_orders, df_orders_items, df_products

print(yellow('orders/'), cc, df_orders.columns.tolist(), rest)
print(df_orders, nl)

print(yellow('orders-items/'), cc, df_orders_items.columns.tolist(), rest)
print(df_orders_items, nl)

print(yellow('products/'), cc, df_products.columns.tolist(), rest)
print(df_products, nl)

### find all clients w/ DS as initials

def is_ds(name: str) -> str:
    return 'DS' in ''.join(_[0].upper() for _ in name.split())# == 'DS'#'JP'

checked_ds = df_customers['name'].apply(lambda _: is_ds(_))
customers_ds = df_customers[checked_ds]
print(yellow('clients/ds'), nl, customers_ds, nl)
print(yellow('clients/ds/list'), ' - '.join(customers_ds['name'].tolist()), nl)

### find orders happened in 2017

checked_2017 = df_orders['ordered'].str.contains('2017')
orders_2017 = df_orders[checked_2017]
print(yellow('orders/2017'), nl, orders_2017, nl)

### MERGE customers_ds and orders_2017

ds_2017 = pd.merge(customers_ds, orders_2017, on='customerid')
print(yellow('ds/2017'), nl, ds_2017, nl)
print(yellow('ds/2017/headers'))
print(cc + '\n'.join(ds_2017.columns.tolist()), nl)

### find one client w/ the most deals 

ds_order_count = ds_2017['name'].value_counts()
print(yellow('count/'), nl, ds_order_count, nl)

### find bagel_coffee sku

bagel = df_products['desc'].str.contains('bagel', case=False)
coffee = df_products['desc'].str.contains('coffee', case=False)
bagel_coffee = df_products[bagel | coffee]
print(yellow('bagel_coffee/entry'), nl, bagel_coffee)
print(yellow('bagel_coffee/sku'), nl,
    cc, bagel_coffee['sku'].tolist(), rest)

### MERGE bagel_coffee and orders_items on column 'sku'
### MERGE coffee_orders and ds_2017 on column 'orderid'

# orders_coffee = pd.merge(bagel_coffee, df_orders_items, on='sku')
orders_coffee = pd.merge(df_orders_items, bagel_coffee, on='sku')
print(yellow('bagel_coffee/orders \n'), orders_coffee, nl)

# bagel_coffee_ds_2017 = pd.merge(orders_coffee, ds_2017, on='orderid')
bagel_coffee_ds_2017 = pd.merge(ds_2017, orders_coffee, on='orderid')
print(yellow('ds/bagel_coffee/2017 \n'), bagel_coffee_ds_2017, nl)
print(bagel_coffee_ds_2017[[
    'name', 'address', 'citystatezip', 'phone', 'sku', 'desc']],
    green('/ends'))
