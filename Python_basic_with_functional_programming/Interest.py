principal = int(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in percentage): "))
time_in_years = int(input("Enter the time (in years): "))

# Convert rate of interest from percentage to decimal
rate_of_interest = rate_of_interest / 100

# Calculate simple interest
simple_interest = (principal * rate_of_interest * time_in_years)

# Calculate total amount
total_amount = simple_interest + principal

print("Simple Interest:", simple_interest)
print("Total Amount:", total_amount)
