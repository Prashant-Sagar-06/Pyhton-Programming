first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Swapping the values of the variables using tuple unpacking
first_number, second_number = second_number, first_number

print("After swapping:")
print("First number:", first_number)
print("Second number:", second_number)
