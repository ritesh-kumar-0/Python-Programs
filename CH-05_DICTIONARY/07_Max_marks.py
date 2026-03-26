#Find Maximum marks of student 
marks = {"Ritesh": 85, "Aman": 90, "Rahul": 78}

max_student = max(marks, key=marks.get)

print("Topper:", max_student)