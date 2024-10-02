import pandas as pd

df = pd.read_csv('unclean_csv.csv')
print(df.columns)
df.columns = df.columns.str.upper()
print(df.columns)
