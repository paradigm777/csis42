# Program name: p14.py
# Your Name: 
# Python Version: 3.6.4
# Date: 01/17/2018
# Description: 	Write a program that asks the user for day and month of a birthday.
#               The program then tells the Zodiac signs that will be compatible with that birthday.
#				
# 				Example for  Aries	The Ram		Mar. 21–Apr. 19	
#				day = 24  # user enters this
#				month = 3 # user enters this
#				if ( month == 3 and day >=21) or (month == 4 and day <= 19):
#				print("You are Aries, Fire group, compatible with Aries, Leo, Sagittarius")
#
# Ask the user for input
d = int(input('Please enter day of birth: '))
m = int(input('Please enter month of birth: '))

# use integer division to get a whole number for quarters
if ( month == 3 and day >=21)

# if there are any quarters...
if q > 0:
    # ...show them...
    print('You have', q, 'quarters')
    #... and subtract the quarters from totalCents
    totalCents = totalCents - q * 25

# use integer division to get a whole number for dimes
d = int(totalCents/10)

# if there are any dimes
if d > 0:
    # ...show them...
    print('You have', d, 'dimes')
    #... and subtract the dimes from totalCents
    totalCents = totalCents - d * 10
    
# use integer division to get a whole number for nickels
n = int(totalCents/5)

# if there are any nickels
if n > 0:
    # ...show them...
    print('You have', n, 'nickels')
    #... and subtract the nickels from totalCents
    totalCents = totalCents - n * 5
    
# use integer division to get a whole number for nickels
p = int(totalCents/1)

# if there are any pennies
if p > 0:
    # ...show them...
    print('You have', p, 'pennies')
    #... and subtract the pennies from totalCents
    totalCents = totalCents - n * 1

'''
C:\python\python3 p13.py
Please enter the total cents: 66
You have 2 quarters
You have 1 dimes
You have 1 nickels
You have 1 pennies

C:\python\python3 p13.py
Please enter the total cents: 16
You have 1 dimes
You have 1 nickels
You have 1 pennies

C:\python\python3 p13.py
Please enter the total cents: 6
You have 1 nickels
You have 1 pennies

C:\python\python3 p13.py
Please enter the total cents: 4
You have 4 pennies

    
    
