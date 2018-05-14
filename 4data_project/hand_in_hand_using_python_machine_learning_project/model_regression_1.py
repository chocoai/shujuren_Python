import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')

print(df.head())

df1 = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df1['HL_PCT'] = (df1['Adj. High'] - df1['Adj. Low']) / df1['Adj. Close'] * 100.0
df1['PCT_change'] = (df1['Adj. Close'] - df1['Adj. Open']) / df1['Adj. Open'] * 100.0
df2 = df1[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
print(df2.head())

