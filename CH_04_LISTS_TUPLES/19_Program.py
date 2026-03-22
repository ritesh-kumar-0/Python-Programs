#WAP to accept marks of 6 students and display them in a sorted manner.
marks = []

for i in range(6):
    m = int(input(f"Enter marks of student{i+1}: "))
    marks.append(m)

    #Sorting the list 
marks.sort()

print("Sorted Marks: ", marks)