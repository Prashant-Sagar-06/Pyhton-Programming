principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate of interest: "))
time = int(input("Enter the time period (in years): "))

# Calculate the simple interest and total amount
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

# Display the simple interest and total amount
print("Simple Interest:", simple_interest)
print("Total Amount:", total_amount)
