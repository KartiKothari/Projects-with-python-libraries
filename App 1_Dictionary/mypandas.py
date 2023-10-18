import pandas
df1=pandas.DataFrame([[2,5,9],[10,87,26]],columns=["Price","Value","Rate"])
print(df1)
df2=pandas.DataFrame([{"Name":"Kartik","Surname":"Kothari"},{"Name":"Jimmy"}])
print(df2)

#print(dir(df1))
print(df1.mean())
print(df1.max().max())
