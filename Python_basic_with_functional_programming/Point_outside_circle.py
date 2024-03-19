# Get input from the user for coordinates and radius of the circle
x1 = int(input("Enter x-coordinate of the center of the circle: "))
y1 = int(input("Enter y-coordinate of the center of the circle: "))
x2 = int(input("Enter x-coordinate of the point: "))
y2 = int(input("Enter y-coordinate of the point: "))
radius = int(input("Enter the radius of the circle: "))

# Calculate the distance between the center of the circle and the point
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Check if the point is inside the circle or not
if distance < radius:
    print("The point is inside the circle.")
elif distance == radius:
    print("The point is on the circle.")
else:
    print("The point is outside the circle.")
