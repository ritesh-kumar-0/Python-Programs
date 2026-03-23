
student = {"Name":"Ritesh", "Age":19, "Course":"CSE"}

print(student.get("Name"))    # Ritesh
print(student.get("collage"))  # output: None

#update the dictionary with elements
student.update({"Collage":"Shoolini University"})
print(student)  #{'Name': 'Ritesh', 'Age': 19, 'Course': 'CSE', 'Collage': 'Shoolini University'}

 