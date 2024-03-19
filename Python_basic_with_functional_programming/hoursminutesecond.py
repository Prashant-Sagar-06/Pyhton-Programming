total_seconds = int(input("Enter the total number of seconds: "))

# Calculate the number of days and remaining seconds
days = total_seconds // (60 * 60 * 24)
remaining_seconds = total_seconds % (60 * 60 * 24)

# Display the number of days and remaining seconds
print("Number of days:", days)
print("Remaining seconds:", remaining_seconds)
