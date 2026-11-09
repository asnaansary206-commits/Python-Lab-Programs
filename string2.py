str=input("enter the string")
if str[-3:]=='ing':
    str=str+'|Y'
else:
    str=str+'|ng'
    print("new string is",str)