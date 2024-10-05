import pandas as pd

df = pd.read_csv('unclean_csv.csv')
print(df.columns)
df.columns = df.columns.str.lower()
print(df.columns)
df = df.rename(columns = {'duration':'TIME'}) # case sensitive
#df = df.rename(columns={'oldname':'newname','oldname2':'newname2'})
print(df.columns)

pd.set_option('display.max_columns', None)
print(df.isnull().sum())

print(df.head(5))