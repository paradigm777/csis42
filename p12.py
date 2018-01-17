# Program name: p12.py
# Name: 
# Python Version: 3.6.4
# Date: 01/16/2018
# Description: 	Write a program to determine if the user can vote. 
#				The program will ask the user a series of questions - age, citizenship 
#               and registration. The user will receive a message as to whether or not 
#               s/he may vote -- yes, no (with a reason - too young, not a citizen, hasn't 
#               registered to vote).
#
#               Be sure to test your program at least 4 times:
#               1. The user can vote
#               2. The user can't vote because they are not old enough.
#               3. The user can't vote because they are not old enough and not a citizen.
#               4. The user can't vote because they are not old enough, not a citizen, not registered.
#
#               Note: You must be over 18, registered , and a citizen to vote.  

# ask the user for input
age = int(input('Please enter your age: '))
citizen = input('Are you a citizen? (y/n): ')
registered = input('Are you registered? (y/n): ')

# check if they can vote
if age >= 18 and citizen == 'y' and registered == 'y':
    print('Congratulations,  you can vote!')

# if they can't vote
else:
    print('Sorry you cannot vote')
    # give the reason(s) why they can't 
    if age < 18:
        print('-You are not old enough')
    if citizen != 'y':
        print('-You must be a citizen')
    if registered != 'y':
        print('-You must be registered')
    
'''
C:\python\python3 p12.py
Please enter your age: 18
Are you a citizen? (y/n): y
Are you registered? (y/n): y
Congratulations,  you can vote!

C:\python\python3 p12.py
Please enter your age: 15
Are you a citizen? (y/n): y
Are you registered? (y/n): y
Sorry you cannot vote
-You are not old enough

C:\python\python3 p12.py
Please enter your age: 15
Are you a citizen? (y/n): n
Are you registered? (y/n): y
Sorry you cannot vote
-You are not old enough
-You must be a citizen

C:\python\python3 p12.py
Please enter your age: 15
Are you a citizen? (y/n): n
Are you registered? (y/n): n
Sorry you cannot vote
-You are not old enough
-You must be a citizen
-You must be registered
'''
	