
class Shape:
    def __init__(self,side1,side2):
        self.side1=side1
        self.side2=side2
    def area(self):
        return self.side1*self.side2
    def perimeter(self):
        return 2*(self.side1 + self.side2)  



class Rectangle(Shape):
    def __init__(self,length,breadth):
       super().__init__(length,breadth)
       
class Square(Shape):
    def __init__(self, side,):
        super().__init__(side, side)       



    #Driver code
l = int(input("ENTER LENGTH "))
b= int(input("ENTER BREADTH "))
rec =Rectangle(l,b)
area=rec.area()
peri=rec.perimeter()
print(f'Area of rectangle with dimensisons {l} and {b} is {area}')
print(f'Perimeter of rectangle with dimensisons {l} and {b} is {peri}')

                