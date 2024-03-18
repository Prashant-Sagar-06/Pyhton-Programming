import numpy as np
lst = list(map(str, input().split()))

array_3x3 = np.array(lst).reshape(3, 3)
print(array_3x3)
