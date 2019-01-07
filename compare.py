import pandas as pd
import numpy

print("hi...")

df1 = pd.read_csv("data1.csv")
df2 = pd.read_csv("data2.csv")

df1Shape = df1.shape[0]
df2Shape = df2.shape[0]

if (df1Shape == df2Shape):
    df = pd.concat([df1, df2, df2]).drop_duplicates(keep=False)
    print("df ", df)
else:
    print("different dataframe")