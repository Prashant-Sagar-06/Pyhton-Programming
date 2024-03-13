#this programm tell that the given no is even or odd without using if and else
number = int(input("Enter a number: "))
result = ("Even", "Odd")[number % 2]
print(f"The number {number} is {result}.")
