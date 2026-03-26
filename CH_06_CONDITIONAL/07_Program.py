'''WAP to find out whether a student has passed or faild if it require
a total of 40% at least 33% in each subject to pass . Assume  3 subject
and take marks as an input from the user '''
 
sub1 = int(input("Enter marks in subject 1:"))
sub2 = int(input("Enter marks in subject 2:"))
sub3 = int(input("Enter marks in subject 3:"))

#calculate total and percentage 
total = sub1 + sub2 + sub3
total_percentage  = (total/300)*100

#check
if(total_percentage >= 40) and (sub1 >=33) and (sub2 >= 33) and (sub3 >= 33):
    print("Student has PASSED")
else:
    print(" Student has Faild!")

print("Total Percentage :", total_percentage)