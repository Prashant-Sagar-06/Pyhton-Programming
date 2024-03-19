Age = int(input("Enter your age: "))
check = Age >= 18
result = 'eligible' * check + 'not eligible' * (1 - check)
print("Your age is",result)
