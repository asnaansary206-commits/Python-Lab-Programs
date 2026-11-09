
class rectangle:
     def __init__(self,length,width):
           self._length=length
           self._width=width
     def area(self):
          return self._length*self._width
     def __lt__(self,other):
           return self.area()<other.area()
r1=rectangle(10,5)
r2=rectangle(6,4)
if r1 < r2:
    print("rectangle 1 has smaller area")
else:
    print("rectangle 1 has larger area or equal area")
print("area of rectangle",r1.area())
print("area of rectangle",r2.area())