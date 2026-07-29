#GAME - SNAKE,WATER OR GUN 

#import random module to let computer choose randomly
import random
choices = ["Snake","Water","Gun"]

#Score Variable 
user_score = 0
computer_score = 0

print("Welcome to Snake Water Gun Game: ")
print("You will play 5 rounds.\n")

#Loops for 5 round 
for round in range(1, 6):
    print(f"\n--------ROUND{round}--------")

#Computer choose randomly
    computer = random.choice(choices)
#User input 
    user = input("Enter Snake, Water or Gun ").capitalize()

    #Check vaild input 
    if user not in choices:
        print("Invaild Choice! Round Skipped.")
        continue
    print("Computer cose:", computer)

    #If both choose same 
    if user == computer:
        print("Is's a Draw!")
    #User win condition 
    elif (user == "Snake" and computer == "Water") or \
         (user == "Water" and computer == "Gun") or \
         (user == "Gun" and computer == "Snake"):

        print("You Win this Round !")
        user_score += 1
#Computer wins
    else:
        print("Computer Wins this Round!")
        computer_score += 1

    #Show current score 
    print(f"Score -> You: {user_score} | computer: {computer_score}")

#Final Result 
print("\n==========FINAL RESULT==========")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("Congratulation! You Won the Game!")

elif computer_score > user_score:
    print("Computer Won the Game !")
else:
    print("The Game is Draw !")

