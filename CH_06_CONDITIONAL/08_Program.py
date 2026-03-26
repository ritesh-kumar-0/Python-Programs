'''A spam comment is defined as a text contaning following Keywords:
"Make a lot of money", "By Now", "Subscribe this", "Click here
WAP to detect these spams"'''

p1 = "Make a lot of money"
p2 = "By Now"
p3 = "Subscribe this"
p4 = "Click here"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message ) ):
    print("This comment is a spam!")
else:
    print("Not a Spam")