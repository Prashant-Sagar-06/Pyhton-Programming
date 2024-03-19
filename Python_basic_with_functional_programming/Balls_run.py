num_sets = int(input("Enter the number of sets: "))

total_balls = num_sets * 6

# Calculating the total number of balls considering the bonus for the last set
balls_with_bonus = (total_balls - (num_sets - 1)) * 6

# Calculating the total number of balls considering the extra balls from sets except the last one
balls_without_bonus = (num_sets - 1) * 3

# Calculating the final total number of balls
final_total_balls = balls_with_bonus + balls_without_bonus

# Displaying the final total number of balls
print("The total number of balls is:", final_total_balls)
