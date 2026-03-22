#Indexing list 

#Write a program to print first and last element of a list.

list = [12, 15, 17, "Ritesh", "Apple"]
print("First & Last:", list[0],list[-1])     # output: 12, Apple


#Print the middle element of a list.
mid = len(list) // 2
print("Middle Element:", list[mid])      #output: 17

#Print last 3 elements using negative indexing.
print(list[-3:])          #output: [17, 'Ritesh', 'Apple']

#Print first 4 elements using slicing.
print("First 4 Elements:",list[0:4])       #[12, 15, 17, 'Ritesh']

#Reverse list using indexing.
print(list[: :-1])                # ['Apple', 'Ritesh', 17, 15, 12]