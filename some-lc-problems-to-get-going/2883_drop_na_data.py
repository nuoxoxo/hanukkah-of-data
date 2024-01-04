import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # way 3
    return students.dropna( axis=0, inplace=True, subset=['name'] )
    # (verbose) (axis 0 : rows, axis 1 : cols)

    # way 2
    return students[ ~students['name'].isna() ]
    # way 1
    return students.dropna( subset='name' )
