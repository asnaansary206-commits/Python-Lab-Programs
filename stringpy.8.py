str=input("enter the string:")
search=input("enter the word to be searched:")
x=str.split(" ")
count=0
for i in x:
  if(i==search):
     count=count+1
print("total occurrences of the word is:",count)