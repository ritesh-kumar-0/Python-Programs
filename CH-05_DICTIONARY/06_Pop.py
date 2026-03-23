
student = {'Name': 'Ritesh', 'Age': 19, 'Course': 'CSE', 'Collage': 'Shoolini University'}
# dict.pop()
#Removes the item with the specified key and returns its value 
value = student.pop("Age")     # value to store Removed value 
print("Removed value", value)  # Removed value: 19
print(student)   #{'Name': 'Ritesh', 'Course': 'CSE', 'Collage': 'Shoolini University'}

#dict.popitem()
#Removes and return the last inserted key-value pair as a tuple 

removed = student.popitem()
print("Removed item:", removed)
print(student )

