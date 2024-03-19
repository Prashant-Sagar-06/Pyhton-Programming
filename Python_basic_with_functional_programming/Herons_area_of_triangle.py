side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

# Calculating the semi-perimeter
semi_perimeter = (side_a + side_b + side_c) / 2

# Calculating the area of the triangle using Heron's formula
area_of_triangle = (semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c)) ** 0.5

# Displaying the area of the triangle
print("The area of the triangle is:", area_of_triangle)
