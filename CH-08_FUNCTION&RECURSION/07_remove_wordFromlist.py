#Write a python function to remove a given word from a list and strip it at the same time.

# Function to remove a given word and strip extra spaces
def remove_word(words, word):

    # Create an empty list to store the final result
    new_list = []

    # Loop through every item in the list
    for item in words:

        # Remove spaces from the beginning and end
        item = item.strip()

        # Check if the current item is NOT the word to remove
        if item != word:

            # Add the cleaned item to the new list
            new_list.append(item)

    # Return the new list
    return new_list


# Original list
words = ["  Ritesh  ", " Apple ", " Banana ", "Ritesh", " Mango "]

# Word that we want to remove
word = "Ritesh"

# Call the function
result = remove_word(words, word)

# Print the final list
print(result)