'''"Make a lot of money", "By Now", "Subscribe this", "Click here
WAP to detect these spams"'''

# Take input from user
comment = input("Enter your comment: ")

# Define spam keywords
spam_keywords = ["Make a lot of money", "Buy Now", "Subscribe this", "Click here"]

# Convert comment to lower case for case-insensitive checking
comment_lower = comment.lower()

# Check for spam
is_spam = False

for word in spam_keywords:
    if word.lower() in comment_lower:
        is_spam = True
        break

# Output result
if is_spam:
    print("This is a SPAM comment !")
else:
    print("This is NOT a spam comment ")