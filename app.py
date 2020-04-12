import os
import pandas as pd
from fn import get_data as data

covid = data.DailyData()
covid.main()

df = covid.dataframe()

df['date'] = pd.to_datetime(df['date'])

df.set_index(df['date'], inplace=True)
df = df.drop(columns=['date'])
#df = df['country_region'].to_string()
print(df.head())
print(df.dtypes)
