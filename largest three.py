n1=int(input("enter first the number: "))
n2=int(input("enter second the number: "))
n3=int(input("enter third the number: "))
if(n1>n2) and(n2>=n1):
    largest=n1
elif(n2>n1)and(n2>=n3):
    largest=n2
else:
    largest=n3
print("the largest number is",largest)