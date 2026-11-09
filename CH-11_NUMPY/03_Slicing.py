import numpy as np
# Creating a NumPy array
arr = np.array([2,3,4,5,6,7,8])

# Creating a NumPy array
print(arr[1:4])    #output:[3 4 5]
#Start slicing from index 2
print(arr[2:])     #Output :[4 5 6 7 8]
#Slice up to index 4
print(arr[:4])        #Output :[2 3 4 5]
#the complete array
print(arr[:])       #Output : [2 3 4 5 6 7 8]
#Using Step 
print(arr[::2])   #Output : [2 4 6 8]
#reverse Array 
print(arr[::-1]) #Output: [8 7 6 5 4 3 2]