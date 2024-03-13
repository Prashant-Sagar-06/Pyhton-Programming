amount = int(input("Enter the total amount: "))

# Subtracting 100 from the amount as we're considering 100 as the base amount
remaining_amount = amount - 100

# Counting the number of 2000 rupee notes
count_2000 = remaining_amount // 2000
remaining_amount -= count_2000 * 2000

# Counting the number of 500 rupee notes
count_500 = remaining_amount // 500
remaining_amount -= count_500 * 500

# Counting the number of 100 rupee notes
count_100 = remaining_amount // 100

print("Number of 2000 rupee notes:", count_2000)
print("Number of 500 rupee notes:", count_500)
print("Number of 100 rupee notes:", count_100)
