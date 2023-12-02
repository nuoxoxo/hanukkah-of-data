import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # print(type(employees.head), '<--- will be <class> \'method\'')
    return employees.head(3)
