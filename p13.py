# Program name: p13.py
# Your Name: 
# Python Version: 3.6.4
# Date: 01/16/2018
# Description: 	Write a program to convert any given number of total cents (under 100)
#               into the correct number of: quarters, dimes, nickels, pennies.
#
#               Hint, use integer casting, 66/25 equals 2.64, but int(66/25)=2.
#               # Test 66, 16, 6, 4
# Ask the user for input
totalCents = int(input('Please enter the total cents: '))

# use integer division to get a whole number for quarters
q = int(totalCents/25)

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

    
    
