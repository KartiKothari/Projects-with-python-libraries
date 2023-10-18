import json                                         #It present
data = json.load(open("data.json",'r'))             #Load method is used convert json into python dictionary
print(data["rain"])
s=0
# for i in data:
#     print(i)
#     print(type(i))          str
#     s=s+1
#     if(s>10):
#         break
name = (input("Enter word which you want to find meaning/defination: "))
print(name)
name=name.lower()
print(name)
for i in data:
  if i == name:                 #Finding the right one
    print(data[name])
    s=s+1
  else:
    continue
if name in data:
  pass
else: print("Please check")
  
if (s!=1):                    #For name which are not presented in datas
  print("€Invalid")  

