#Boolean Masking 
''' Boolean masking in NumPy is a technique used to filter an array based on a condition. 
It returns only those elements that satisfy the given condition.'''

import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Creating a Boolean mask
mask = arr % 2 == 0

# Printing only even elements
print(arr[mask])