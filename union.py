import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta, timedelta

list_fiels_by_year = os.listdir('Data consuption of year')

path_to_file = os.path.join('Data consuption of year', list_fiels_by_year[0])

list_csv_for_year = os.listdir(path_to_file)
path_to_csv = os.path.join(path_to_file, list_csv_for_year[0])
path_to_csv_1 = os.path.join(path_to_file, list_csv_for_year[0+1])
df = pd.read_csv(path_to_csv, sep=';')
df_1 = pd.read_csv(path_to_csv_1 , sep=';')

date_end = df.iloc[-1]['DateTime']
date_start = df_1.iloc[0]['DateTime']

date_end = datetime.strptime(date_end, "%Y-%m-%d %H:%M:%S")
date_start = datetime.strptime('2016-06-20 00:50:00', "%Y-%m-%d %H:%M:%S")

interval = date_start - date_end
interval = int((interval.total_seconds() / 60.0) / 5)
if interval > 1:
    date = date_end
    list_date = []
    for i in range(interval-1):
        date += timedelta(minutes=5)
        list_date.append(date)
print(interval)
print(list_date)
