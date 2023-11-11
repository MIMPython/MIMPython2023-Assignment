import pandas as pd
from datetime import datetime, timedelta
import random
random.seed(55)
# create a timestamp column
timestamp = []
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

total_seconds = (end_date - start_date).total_seconds()
timestamp = [start_date +
             timedelta(seconds=random.randint(0, total_seconds)) for _ in range(1000)]

df = pd.DataFrame({'timestamp': timestamp})

date = [df['timestamp'][i].date() for i in range(1000)]
# df['date'] = df['timestamp'].dt.date
df['date'] = date
print(df)
print(df.dtypes)
'''
              timestamp        date
0   2022-02-05 02:01:42  2022-02-05
1   2022-03-18 05:09:09  2022-03-18
2   2022-02-28 05:49:53  2022-02-28
3   2022-10-15 03:25:52  2022-10-15
4   2022-04-28 13:15:26  2022-04-28
..                  ...         ...
995 2022-10-26 01:28:15  2022-10-26
996 2022-09-19 20:25:23  2022-09-19
997 2022-06-12 18:26:47  2022-06-12
998 2022-12-18 14:47:37  2022-12-18
999 2022-04-11 21:01:44  2022-04-11

[1000 rows x 2 columns]
timestamp    datetime64[ns]
date                 object
dtype: object
'''
df.to_csv('additionalFolder/module08_assignment03_student06_NguyenThiMen_data.csv')
