# Multiple List Methods in One Code 

marks = [78, 55, 56, 89, 45, 60]

# Add a new mark
marks.append(92)       # Add at end
print("After append:", marks)     # output: After append: [78, 55, 56, 89, 45, 60, 92]


# Insert a mark at index 2
marks.insert(2, 67)    # Insert at specific position
print("After insert:", marks)   #Output:  After insert: [78, 55, 67, 56, 89, 45, 60, 92]


#Remove a failed mark (45)
marks.remove(45)    # Remove that value 
print("After remove:", marks)    #After remove: [78, 55, 67, 56, 89, 60, 92]

# Add marks of another student
marks.extend([81, 74]) # Add multiple values
print("After extend:", marks)

# Sort marks (ascending order)
marks.sort()
print("After sort:", marks)

# Reverse to get highest marks first
marks.reverse()
print("After reverse:", marks)

# Count how many times 78 appears
print("Count of 78:", marks.count(78))

# Find index of 89
print("Index of 89:", marks.index(89))
# Final list
print("Final Marks List:", marks)
