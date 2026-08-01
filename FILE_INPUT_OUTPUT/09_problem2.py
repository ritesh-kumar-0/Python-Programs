'''Q2. The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score.'''

import random

def game():
    print("==== YOU ARE PALYING THE GAME ====")

#Generate a random score 
    score = random.randint(1, 100)
    return score
#Call the function 
score = game()

#Fetch the hiscore 
with open("FILE_INPUT_OUTPUT/hiscore.txt", "r") as file:
    hiscore = file.read()
#if the file is blank , set the high score to 0
    if(hiscore != ""):
        hiscore = int(hiscore)
    else:
        hiscore = 0

#compare the current score with the previous high score 
    if score > hiscore:
        print("New High Score!" , score)
 # Open the file in write mode and update the high score
        with open("FILE_INPUT_OUTPUT/hiscore.txt", "w") as file:
            file.write(str(score))
    else:
        print("Your Score:", score)
        print("High Score:", hiscore )
        