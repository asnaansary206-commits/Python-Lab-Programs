dict={}
n=int(input("enter the number of element:"))
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    dict[key]=value
print("the dictionary is",dict)
dict_asc=sorted(dict.items())
print("dictionary in ascendingorder:",dict_asc)
dict_desc=sorted(dict.items())
print("dictionary in descendingorder:",dict_desc)
