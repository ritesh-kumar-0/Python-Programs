#THE PERFECT GUESS 
'''We are going to write a program that generates a random number and asks the user to
guess it.
If the playerʼs guess is higher than the actual number, the program displays “Lower
number please” .
Similarly, if the userʼs guess is too low, the program prints “Higher number please” .
When the user guesses the correct number, the program displays the number of
guesses the player used to arrive at the number'''

import random 

#generate a random number between 1 to 100.
number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Guess the number: "))
    guesses += 1

    if guess > number:
       print("Lower number please")

    elif guess < number:
         print("Higher number please")

    else:
        print("Correct! You gussed the Number.")
        break

print(f"You guessed the number in{ guesses} guesses.")