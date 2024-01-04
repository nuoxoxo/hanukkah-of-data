import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:

    # way 2
    employees[ 'salary' ] *= 2
    return employees

    # way 1
    def foreach( row ):
        row['salary'] *= 2
        return row
    return employees.agg(foreach, axis=1)
