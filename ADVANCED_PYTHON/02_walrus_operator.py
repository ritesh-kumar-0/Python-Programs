#Suppose we're building a program that reads data from a user until they enter "quit".
# Without walrus (:=)
'''command = input("Enter command: ")

while command != "quit":
    print("You entered:", command)
    command = input("Enter command: ")
'''


#With walrus 

while (command := input("Enter command: ")) != "quit":
    print("You entered:", command)