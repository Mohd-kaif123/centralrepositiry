# To Install: sudo apt install python3-pandas
import pandas as pd

df=pd.read_csv('data.csv')
print(df.head())
print(df[df['price']>150000])
sort=df.sort_values(by='price',ascending=False)
print("\n Sorted DataFrame:\n", sort)
