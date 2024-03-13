#This Programm takes input from user and chnge it into hours minutes and seconds accordingly
seconds = int(input("Enter the number of seconds: "))

hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(f"{seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")
