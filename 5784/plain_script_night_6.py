import pandas as pd

df_order_items = pd.read_csv('./noahs-orders_items.csv')
df_orders = pd.read_csv('./noahs-orders.csv')
df_prod = pd.read_csv('./noahs-products.csv')
df_customers= pd.read_csv('./noahs-customers.csv')

# looking for a possibly existing smallest margin
prices = pd.merge(df_order_items, df_prod, on='sku')
prices['margin'] = prices['qty'] * prices['unit_price'] - prices['qty'] * prices['wholesale_cost']

# look this person up ~ female

df_final = pd.merge(prices, df_orders, on='orderid')
df_final = pd.merge(df_final, df_customers, on='customerid')
res = df_final.groupby(['name','phone','birthdate','address','citystatezip']).agg({'margin': 'sum'}).sort_values(by='margin').head(3)

print( res, '/res' )
