import json
data = json.load(open("data.json"))
for_once=False
def translate(w):
    w=w.lower()

    from difflib import get_close_matches
    from difflib import SequenceMatcher

    if w in data:
        return data[w]
    elif (len(get_close_matches(w,data.keys()))>0):
        yn = input(("Did you mean %s instead? press Y if yes or N for no :") %get_close_matches(w,data.keys())[0])
        if yn=="Y": 
            return(data[get_close_matches(w,data.keys())[0]])
            
        # elif yn=="N": 
        #     return("Please1 check, Word is not right")
        else:
            return("Please check, Word is not right")
    else:
        return("Please check, Word is not right")

word = input("Enter Word: ")
output = translate(word)
if(type(output)==list):
    print(output[0])
#   for item in output:
#     print(item)
else:
    print(output)
print(type(translate(word)[0]))

# s=(SequenceMatcher(None,w,data.keys()).ratio)
#     if(s>"0.77"):
#         g=get_close_matches(w,data.keys())[0]
#         print("Yes i am in")
#         if(len(g)>1):
#             print(f"Do you mean '{g}'")
#             k=input("Press Y or N ")
#             if(k=="Y"):
#               print("oh yeah")
#               return translate(g)
#     else: return("Please check, Word is not right") 