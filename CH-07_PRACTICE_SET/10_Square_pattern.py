'''Write a program to print the following star pattern
* * * *
*     * 
* * * *  for n = 4 '''
n = int(input("Enter the Number of columns: "))
row = 3

#outer loop for rows
for i in range(row):
#inner loop for columns
    for j in range(n):
        if i ==0 or i == row - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
