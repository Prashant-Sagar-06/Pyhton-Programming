amount = int(input("Enter the amount: "))

# Calculating the amount after subtracting 100
remaining_amount = amount - 100

# Calculating the number of 2000 rupee notes
num_2000_notes = remaining_amount // 2000

# Calculating the remaining amount after considering 2000 rupee notes
remaining_amount -= num_2000_notes * 2000

# Calculating the number of 500 rupee notes
num_500_notes = remaining_amount // 500

# Calculating the remaining amount after considering 500 rupee notes
remaining_amount -= num_500_notes * 500

# Calculating the number of 100 rupee notes
num_100_notes = remaining_amount // 100

# Displaying the number of each type of notes
print("Number of 2000 rupee notes:", num_2000_notes)
print("Number of 500 rupee notes:", num_500_notes)
print("Number of 100 rupee notes:", num_100_notes)
