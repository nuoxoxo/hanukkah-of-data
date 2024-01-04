import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # way 2
    students['grade'] = students[['grade']].astype( int )
    return students
    
    # way 1
    return students.assign(
        grade=students['grade'].astype(int)
    )
