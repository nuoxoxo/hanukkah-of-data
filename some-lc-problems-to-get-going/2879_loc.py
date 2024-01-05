import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:

    # idea - [ select from studs where id = 101; ] [ select col 'name', 'age' from previous ]

    # way 3
    return students.loc[
        students["student_id"] == 101,
        "name":
    ]

    # way 2
    return students.loc[
        students["student_id"] == 101,
        ['name', 'age']
    ]

    # way 1
    return students.loc[students["student_id"] == 101][
        ['name', 'age']
    ]
