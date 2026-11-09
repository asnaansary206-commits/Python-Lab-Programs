numbers=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    num=int(input("enter the number:"))
    numbers.append(num)
print("orginal list:",numbers)
updated_list=[]
for i in range(0,n):
    if numbers[i]%2!=0:
        updated_list.append(numbers[i])
print("updated list:",updated_list)