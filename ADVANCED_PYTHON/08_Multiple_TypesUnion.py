'''Sometimes a variables csn contain more than one type .
for example , an ID might be either an integer or a string '''

# Union 
student_id: int | str = 101
student_id = "CS101"

print(student_id)