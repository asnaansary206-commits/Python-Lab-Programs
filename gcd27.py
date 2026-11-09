def gcd(a,b):
    while b!=0:
        a,b=b,a % b
    return a
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
result=gcd(num1,num2)
print("gcd is:",result)
