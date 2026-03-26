'''WAP to find whether a given username contains less than
10 character or not '''
username = input("Enter username:")

if(len(username)<10):
    print("Your user name contains less than 10 characters")
else:
    print("All is Well")