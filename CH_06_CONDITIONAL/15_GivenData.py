'''Analyze a dataset containing information about renowned athletes, including their names, sports, and notable achievements,
 to apply conditional logic and filtering techniques.
                 Player Name	Sport	Achievements
                
                Serena Williams	 Tennis	   23 Grand Slams
                Lionel Messi	 Soccer	    7 Ballon d'Ors
                Michael Phelps	 Swimming	23 Gold Medals
                Usain Bolt	    Athletics	8 Gold Medals
                Roger Federer	 Tennis	    20 Grand Slams
            Cristiano Ronaldo	 Soccer	    5 Ballon d'Ors'''

'''Q: Write a Python program to check if a player belongs to the sport Tennis or has exactly 20 achievements. 
If the condition is true, print a success message.'''
player_name = "Roger Federer"
sport = "Tennis"
achievements = 20

if sport == "Tennis" and achievements == 20:
    print(f"{player_name} meets the criteria! They play {sport} and have {achievements} achievements.")
else:
    print(f"{player_name}does not meet the criteria.")

#Output: Roger Federer meets the criteria! They play Tennis and have 20 achievements.