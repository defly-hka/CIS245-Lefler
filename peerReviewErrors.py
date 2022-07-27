# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.
#David Lefler
#CIS-245
#July 25, 2022

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()
#1 should break this into multiple print('\n') so reader does not spit back errors

def chooseCave(): 
    cave = ''
#2 cave is indented with spaces instead of tabbed like the rest of the text here
    #inconsistent spacing means it will not read correctly

	while cave != '1' and cave != '2': 
#3 Cave choice does not matter, while loop only specifies what happens if choices are not equal to 1 or 2, not if choices are equal

		print('Which cave will you go into? (1 or 2)')
		cave = input()
#4 cave does not accept user input() means the following while loop does not have any information to base it's logic on

	return caves
#5 caves is an unassigned value, should read 'cave'

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)
#6 chosenCave is never assigned a value/chosen by the user, so the game is not winnable in its current state
#chosenCave or chooseCave need to either share a value or should be used universally

	if chosenCave == str(friendlyCave):
#7 str(friendlyCave) means that the randint generated will not be recognized as an integer, since friendlyCave is already an integer, str() is unecessary

		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'
		#6 print is missing () so this option will not display correctly
playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y':
#8 for while loop to work playAgain == 'yes' or playAgain == 'y': 
#missing extra '=' 

	displayIntro()
	caveNumber = choosecave()
#9 choosecave() is unassigned because python is case sensitive should be chooseCave()
	checkCave(caveNumber)
#10 checkCave, caveNumber, and chooseCave are assigned to the function chooseCave which is not a number/value, but a way to generate a number/integer   
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")
			#thanks for planing typo, not sure if this counts
