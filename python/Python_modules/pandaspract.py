import pandas as pd

'''
version=pd.__version__
print(version)
'''
'''
list=[10, 20, 30, 40, 50]
list1=pd.Series(list)
print(list1)
'''

'''
dict={
    "Name": ["Kaif", "Ali", "Rahul"],
    "Age": [23, 25, 24]
}
dic=pd.DataFrame(dict)
print(dic)
'''
'''
df=pd.read_csv("data.csv")
print(df.head(2))
'''
'''
dict={
    "Name": ["Kaif", "Ali", "Rahul"],
    "Age": [23, 25, 24],
    "City": ["Mumbai","Delhi","Pune"]   
    }
dic=pd.DataFrame(dict)
print(dic)
'''

'''
df=pd.read_csv("data.csv")
print(df.shape)
'''
'''
df=pd.read_csv("data.csv")
print(df.columns)
'''
'''
df=pd.read_csv("data.csv")
print(df.count)
'''

