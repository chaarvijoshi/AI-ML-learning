import pandas as pd

data = {
    "name" : ["charvi","aman","rahul","riya","priya"],
    "age" : [21,21,22,20,22],
    "course" : ["AI","AI","AI","ML","Data Science"],
    "marks" : [88,98,78,67,90]
}

df = pd.DataFrame(data)
print(df)
print(df[["name","marks"]])
print(df[df[("marks")]>85])
print(df.sort_values("marks"))
print(df.sort_values("marks",ascending=False))
print(df["marks"].sum())
print(df["marks"].mean())
print(df["marks"].max())
print(df["marks"].min())

for course , data in df.groupby("course"):
    print(course)
    print(data)
    
id = df.groupby("course")["marks"].mean()
print(id)
    

