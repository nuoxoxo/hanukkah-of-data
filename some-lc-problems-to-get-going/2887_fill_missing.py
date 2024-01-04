import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:

    # way 2 - isnull + iterrows + .at[idx,'key']
    for idx, row in  products.iterrows():
        if not pd.isnull( row['quantity'] ):
            continue
        products.at[ idx, 'quantity' ] = 0
    return products

    # way 1 - using fillna
    return products.fillna(
        value = { 'quantity': 0 }
    )
