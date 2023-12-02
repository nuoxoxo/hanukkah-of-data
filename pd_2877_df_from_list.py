import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # 2
    return pd.DataFrame(student_data, columns=['student_id', 'age'])
    # 1
    """
    cols = ['student_id', 'age']
    res = pd.DataFrame(student_data, columns=cols)
    return res
    """
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
