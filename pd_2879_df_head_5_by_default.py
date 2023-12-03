import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:

    # Way 3 : int-location
    return employees.iloc[0:3]

    # Way 2 : treat DF as list
    return employees[:3]

    # Way 1 : head method
    # print(type(employees.head), '<--- will be <class> \'method\'')
    return employees.head(3)

