#Slicing a 2D Array
#A 2D array contains rows and columns.
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[0:2, 0:2]) #Output :[[10 20]
                      #[40 50]]

''' arr[row_start:row_stop, column_start:column_stop]
  Before comma = Row slicing.
  After comma = Column slicing.'''

#Select the first row
print(arr[0, :])   #output:[10 20 30]

#Select the second column
print(arr[:, 1])   #output:[20 50 80]
#Select the last column
print(arr[:, -1])   #output:[30 60 90]