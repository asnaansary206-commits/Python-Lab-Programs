class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth= breadth
  def area(self):
      return self.length*self.breadth
  def perimeter(self):
      return 2*(self.length+self.breadth)
  def compare(self,other):
      if self.area()>other.area():
          print("first rectangle has larger are")
      elif self.area()<other.area():
        print("second rectangle has larger area")
      else:
        print("both rectangles are equal area")
r1=Rectangle(10,5)
r2=Rectangle(6,4)
print("are of rectangle 1:",r1.area())
print('perimeter of rectangle 1:',r1.perimeter())
print("perimeter of rectangle 2:",r2.area())
print("area of rectangle 2:",r2.perimeter())
r1.compare(r2)

