number=[]
n=int(input("enter the number of elements in the list:"))
for i in range(0,n):
    element=int(input("enter the element:"))
    number.append(element)
print(":positive numbers are:")
for i in range(0,n):
    if(number[i]>0):
        print(number[i])