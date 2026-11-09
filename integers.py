list1= list(map(int,input("enter the first list:").split()))
list2= list(map(int,input("enter the second list:").split()))
if len(list1)>len(list2):
    print("both numbers are the same length")
else:
    print("list do not have the same length")
if sum(list1)==sum(list2):
    print("both numbers are the same sum")
else:
    print("list do not have the same sum")
common=[]
for a in range(1,len(list1)+1):
    if a in list1 and a not in common:
        common.append(a)
if common:
        print("common element in both list are:",common)
else:
        print("no common element in both list")