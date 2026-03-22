#Divide list into two parts using indexing.

list = [1 , 2 , 3, 4, 5, 6, ]

# Find middle index using integer division
mid = len(list) // 2   # 6 // 2 = 3

# Slice first half (from index 0 to mid-1)
first = list[:mid] # [1, 2, 3]

# Slice second half (from mid to end)
second = list[mid:]   # [4, 5, 6]

print(first, second)