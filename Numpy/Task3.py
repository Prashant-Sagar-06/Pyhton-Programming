import numpy as np

N = int(input("Enter the number of rows (N): "))
M = int(input("Enter the number of columns (M): "))

array = np.eye(N, M, dtype=int)

print("Resulting array:")
print(array)
