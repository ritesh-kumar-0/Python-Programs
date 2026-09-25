'''Analyze a dataset containing information about renowned athletes, including their names, sports, and notable achievements,
 to apply conditional logic and filtering techniques.
                 Player Name	Sport	Achievements
                
                Serena Williams	 Tennis	   23 Grand Slams
                Lionel Messi	 Soccer	    7 Ballon d'Ors
                Michael Phelps	 Swimming	23 Gold Medals
                Usain Bolt	    Athletics	8 Gold Medals
                Roger Federer	 Tennis	    20 Grand Slams
            Cristiano Ronaldo	 Soccer	    5 Ballon d'Ors'''

'''Q: Write a Python program to check if a player Lionel Messi has more than 10 achievements. If the condition is true,
 print the player's name, sport, and achievements else print does not have more than 10 achievements'''
player_name = "Lionel Messi"
sport = "Soccer"
achievements = 7

if achievements > 10:
    print(f"{player_name} plays {sport} and has {achievements} achievements")

else:
    print(f"{player_name} does not have more than 10 achievements. ")

#Output : Lionel Messi does not have more than 10 achievements.