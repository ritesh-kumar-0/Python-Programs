'''WAP to calculate the grade of a student from this marks from the following scheme:
    90-100 = Exclent
    80-90 = A
    70-80 = B
    60-70 = C
    50-60 = D
    <50 = Fail'''

marks = int(input("Enter Your Marks: "))

if(marks <= 100 and marks >= 90):
    grade = "Excllent"
elif(marks <90 and marks >= 80):
    grade = "A"
elif(marks < 80 and marks >=70):
   grade = "B"
elif(marks < 70 and marks >=60):
    grade = "C"
elif(marks < 60 and marks >=50):
    grade = "D"
elif(marks <50):
   grade = "Fail"

print ("Your Grade is :", grade)