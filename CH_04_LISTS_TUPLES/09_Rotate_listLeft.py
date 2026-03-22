#Rotate list

list = [1, 2, 3, 4, 5]
#Rotate list left by 1 position 
list = list[1:] + [list[0]]
print(list)         #output: [2, 3, 4, 5, 1]


#Rotate list right by 1 position
list = [list[-1]] + list[:-1]
print(list)   #[1, 2, 3, 4, 5]

