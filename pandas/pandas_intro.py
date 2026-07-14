# Pandas is a Python library used to work with tabular (table-like) data.

import pandas as pd
arr = pd.Series([10,20,30])
print(arr)
data = {
    "name" : ["chaarvi","kritvi"],
    "age"  : [ 21 ,21 ]
}
arr = pd.DataFrame(data)
print(arr)

data = {
    "name" : ["chaarvi", "archi","kritvi"],
    "age" : [21,21,21],
    "course" : ["AI","ML","AI"]
}
df = pd.DataFrame(data)
print(df)
print(df["age"])
print(df[["name","age"]])
print(df.loc[1])
print(df.iloc[2])
print(df["age"]>21)
print(df.sort_values("name"))

print(df.isnull())
for course,data in df.groupby("course"):
    print(course)
    print(data)


