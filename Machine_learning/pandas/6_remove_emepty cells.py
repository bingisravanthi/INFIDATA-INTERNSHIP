import pandas as pd

df=pd.read_csv('data.csv')#loading the dataset
print('[info] data loaded successfully...')

print('[info] checking for NaN values....')
print(df.columns[df.isna().any()])

print('[info] checking NaN values....')
df=df.dropna()#this line remove entire row which has NaN values

print('[info] checking for NaN values again...')
print(df.columns[df.isna().any()])