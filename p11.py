# Program name: p11.py
# Your Name: 
# Python Version: 3.6.3
# Date Started - Date Finished: 01/16/2018
# Description: 	Write a program to simulate rock-paper-scissors game.
#				Each players enters 'R', 'P', 'S' or 1, 2, 3 for Rock, Paper, Scissors.
#
#				The program then shows the winner on the basis of:
#				Paper covers Rock
# 				Rock breaks Scissors
#				Scissors cut Paper
#				Tie

# need this for randint()
import random

# generate two random numbers b/w 1-3
# each player is a random number b/w 1-3
print('Rock, Paper, Scissors')
p1 = int(input('Enter 1, 2, 3 to play rock, paper, or scissors: '))
# p1 = random.randint(1,3)
p2 = random.randint(1,3)

# define variables, rock, paper, scissors
rock = 1
paper = 2
scissors = 3

print('p2 played ' + str(p2))

# 3 cases where p1 can win:
if p1 == rock and p2 == scissors:
	print('p1 wins, rock breaks scissors')
elif p1 == paper and p2 == rock:
	print('p1 wins, paper covers rock')
elif p1 == scissors and p2 == paper:
	print('p1 wins, scissors cuts paper')
	
# 3 cases where p2 can win:	
elif p2 == rock and p1 == scissors:
	print('p2 wins, rock breaks scissors')
elif p2 == paper and p1 == rock:
	print('p2 wins, paper covers rock')
elif p2 == scissors and p1 == paper:
	print('p2 wins, scissors cuts paper')	
elif p2 == p1:
	print('Tie!')
else:
	print('Invalid input.')
	

'''
C:\python>python3 p11.py
Rock, Paper, Scissors
Enter 1, 2, 3 to play rock, paper, or scissors: 1
p2 played 2
p2 wins, paper covers rock

C:\python>python3 p11.py
Rock, Paper, Scissors
Enter 1, 2, 3 to play rock, paper, or scissors: 2
p2 played 2
Tie!

C:\python>python3 p11.py
Rock, Paper, Scissors
Enter 1, 2, 3 to play rock, paper, or scissors: 3
p2 played 1
p2 wins, rock breaks scissors

C:\python>python3 p11.py
Rock, Paper, Scissors
Enter 1, 2, 3 to play rock, paper, or scissors: 1
p2 played 3
p1 wins, rock breaks scissors

C:\python>python3 p11.py
Rock, Paper, Scissors
Enter 1, 2, 3 to play rock, paper, or scissors: 1
p2 played 3
p1 wins, rock breaks scissors
'''
	