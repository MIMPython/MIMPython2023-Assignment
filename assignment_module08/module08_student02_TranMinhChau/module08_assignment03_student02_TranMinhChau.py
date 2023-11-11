# Bài tập 3: DataFrame datetime tricks)
import pandas as pd
import numpy as np

def create_dataframe(start: str, end: str, n: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed=42)
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    origin = start.toordinal()
    days = rng.integers(origin, end.toordinal() + 1, n)
    df = pd.DataFrame({
        "timestamp": pd.to_datetime(days, origin="unix", unit="D"),
        "date": pd.to_datetime(days, origin="unix", unit="D").dt.date
    })
    return df

print(create_dataframe("2022-01-01", "2022-12-31", 1000))
