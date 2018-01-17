# Program name: p09.py
# Your Name: David Flynn
# Python Version: 3.6.3
# Date Started - Date Finished: 01/16/2018
# Description: 	You will write a program to compute a person's height and print out a message
#				The user will input their height in feet and inches.
#				The program will convert the feet and inches into total_inches, and then print a message.
#				If the total inches is greater than 72, the message should be something like, "You're tall."
# 				If the total inches is between 5' and 6', a different message should appear, like "You are average"
#				If the total inches is less than 60, another message should appear, like "You are vertically challenged"



# user inputs height, feet and inches
feet = int(input('Please enter your height feet: '))
inches = int(input('inches: '))

# calculate total_inches
total_inches = feet * 12 + inches

# give user the correct message
if total_inches > 72: 	
	print('You are tall') 
elif total_inches > 60:
	print('You are average')
else:
	print('You are vertically challenged')
# if total_inches is between 60 and 72....show second message
# if total_inches is under 60...show third message


'''
C:\python>python3 p09.py
Please enter your height feet: 6
inches: 1
You are tall

C:\python>python3 p09.py
Please enter your height feet: 5
inches: 4
You are average

C:\python>python3 p09.py
Please enter your height feet: 3
inches: 2
You are vertically challenged
'''
