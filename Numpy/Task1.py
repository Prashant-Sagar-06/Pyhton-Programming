import numpy as np

# Take input as space-separated strings
lst = list(map(str, input().split()))

# Convert the list to a numpy array
arr = np.array(lst)

# Flip the array
flipped_arr = np.flip(arr)

# Print the flipped array
print(flipped_arr)
