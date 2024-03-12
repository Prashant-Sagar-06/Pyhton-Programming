age = int(input("Enter your age: "))
check = age >= 18
result = 'eligible' * check + 'not eligible' * (1 - check)
print(result)
