#This programm find out area of triangle using herons formula
import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

semi = (a + b + c) / 2
area_of_tri = math.sqrt(semi * (semi - a) * (semi - b) * (semi - c))

print("Area of the triangle:", area_of_tri)
