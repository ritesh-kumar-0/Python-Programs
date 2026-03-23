''' WAP to create a dictionary of Hindi Words with values as their 
English translation provide user with an option to look it up!'''

# create the dictionary

hindi_dict = {
    "pustak": "book",
    "ghar": "house",
    "kutta": "dog",
    "billi": "cat",
    "paani": "water"
}

# Show dictionary keys to user
print("Available Hindi Words:", list(hindi_dict.keys()))

# Ask user for a word
word = input("Enter Hindi Word: ").strip().lower()

# Lookup and display the meaning
if word in hindi_dict:
    # using f-string and correct variable name
    print(f"The English meaning of '{word}' is '{hindi_dict[word]}'")
else:
    print("Sorry, That word is not in the dictionary.")