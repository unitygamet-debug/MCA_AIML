import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("retail_sales_dirty.csv")
df=df.fillna({"CustomerID":"None"})
df["Description"]=df["Description"].replace({"HAND WARMER UNION JACK":"KUNAL",
                                             "SET 7 BABUSHKA NESTING BOXES":"Karan"})
df["Description"]=df["Description"].str.lower()

print(df.isnull().sum())
df=df.drop_duplicates()
print(df.isnull().sum())


