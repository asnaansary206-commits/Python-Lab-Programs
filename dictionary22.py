from abc import update_abstractmethods

dict1={}
dict2={}
n1=int(input("enter the number of element in first seconddictionary: "))
for i in range(n1):
    key=input("enter key:")
    value=input("enter value:")
    dict1[key]=value
n=int(input("enter the number of element in second seconddictionary: "))
for i in range(n1):
    key=input("enter value:")
    value=input("enter value:")
    dict2[key]=value
print(dict1)
print(dict2)
dict1.update(dict2)
print("merged dictionary:",dict1)
