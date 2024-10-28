# we have to take input of same side of isoceles triangle and its base and display its area
# also check the validity of triangle if triangle is possible or not
# eg base=8 equal_side=5 area=12 units sq
# try it with your own in any language
import math
a=int(input("enter the length of side "))
b=int(input("enter the base "))
if a+a>b:
    print("your triangle is valid")
    m=a**2-(b/2)**2
    n=math.sqrt(m)
    area=1/2*b*n
    print("area of the triangle is" ,area)
else:
    print("your triangle is not valid")




