import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:

    # way 3 - .index
    temp = []
    for idx in df1.index:
        row = df1.iloc[idx]
        temp.append([
            row['student_id'], row['name'], row['age']
        ])
    for idx in df2.index:
        row = df2.iloc[idx]
        temp.append([
            row['student_id'], row['name'], row['age']
        ])
    return pd.DataFrame(
        temp,
        columns=['student_id', 'name', 'age']
    )

    # way 2 - iloc
    temp = []
    for _, row in df1.iterrows():
        temp.append([
            row['student_id'],
            row['name'],
            row['age']
        ])
    for _, row in df2.iterrows():
        temp.append([
            row['student_id'],
            row['name'],
            row['age']
        ])

    return pd.DataFrame(
        temp,
        columns=['student_id', 'name', 'age']
    )
    
    # way 1 - using .concat
    return pd.concat(
        [df1, df2],
        axis = 0
    )
