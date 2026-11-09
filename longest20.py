list=[]
n=int(input("enter the number of words in the list:"))
for i in range(0,n):
  a=input("enter the words:")
  list.append(a)
print(list)
length=len(list[0])
str=list[0]
for i in range(1,n):
    if(len(list[i])>length):
        str=list[i]
        length=len(str)
print("the longest words",str)
print("the length of the words is",length)