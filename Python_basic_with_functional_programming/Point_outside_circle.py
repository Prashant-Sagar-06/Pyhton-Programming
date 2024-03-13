x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
radius = int(input("Enter radius: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if radius > distance:
    print("Point is inside the circle.")
elif radius == distance:
    print("Point is on the circle.")
else:
    print("Point is outside the circle.")
