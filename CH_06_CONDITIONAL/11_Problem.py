'''WAP which find out whether a given name is present in alist or not '''
list = ["Ritesh", "Viveak","Kundan", "Aryan"]

name = input("Enter your name:")

if(name in list):
    print("Your name is in the list")
else:
    print("User not found!")