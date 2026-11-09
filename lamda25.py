square=lambda side:side * side
rectangle=lambda length,breadth:length * breadth
triangle=lambda base,height:0.5 * base * height
side=float(input("enter a side of the sqaure:"))
print("area of square:",square(side))
length=float(input("enter a length of the rectangle:"))
breadth=float(input("enter a breadth of the rectangle:"))
print("area of rectangle:",rectangle(length,breadth))
base=float(input("enter a base of the triangle:"))
height=float(input("enter a height of the triangle:"))
print("area of triangle:",triangle(base,height))