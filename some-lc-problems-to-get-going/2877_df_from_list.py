import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:

    # way 3
    df = { 'student_id': [], 'age': [] }
    for sid, age in student_data:
        df[ 'student_id' ].append( sid )
        df[ 'age' ].append( age )
    return pd.DataFrame( df )

    # way 2
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

    # way 1

    cols = ['student_id', 'age']
    return pd.DataFrame(student_data, columns=cols)

"""
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
"""
