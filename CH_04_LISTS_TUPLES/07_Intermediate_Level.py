# Intermediate Level Questions 

list = [25, 30, "Ritesh", "Apple", True]

#Swap First and Last Element using indexing 
list[0], list[-1] = list[-1], list[0]
print(list)                    #[True, 30, 'Ritesh', 'Apple', 25]

#Replace element at index 2 with 100.
list[2] = 100
print(list)                  #[True, 30, 100, 'Apple', 25]

#Print elements at even indexes.
print(list[: :2])            #[True, 100, 25]




