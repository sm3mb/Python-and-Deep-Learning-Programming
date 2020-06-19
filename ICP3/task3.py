import numpy as np

# Generating the Random array within the given range
b = np.random.randint(low=1, high=20, size=15)

# making the array of 3 x 5 array
b = b.reshape(3,5)

print('Reshape with 3 X 5',b)
# print(np.max(b, axis = 1).reshape(-1 , 1))

# Finding the max and replacing the it with 0 in each row
result = np.where(b == np.max(b, axis = 1).reshape(-1 , 1), 0, b)

print(result)