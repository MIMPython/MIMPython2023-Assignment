import pandas as pd
import numpy as np

time_random = pd.to_datetime(np.random.choice(pd.date_range('2022-01-01', '2022-12-31', freq ='s'), 1000))# tạo ra một dataframe bằng cách chọn ngẫu nhiên các ngày trong
data = pd.DataFrame({'timestamp': time_random})                                                                          #các ngày từ 2022-01-01 đến 2022-12-31 đến độ chính xác là giây
data['date'] = pd.to_datetime(data['timestamp'].dt.date) #dt.date để lấy ra ngày trong côột date của dataframe
print(data)