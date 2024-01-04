import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    res = weather.pivot(
        index = 'month',
        columns = 'city',
        values = 'temperature'
    )
    return res
