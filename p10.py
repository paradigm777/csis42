# Program name: p10.py
# Your Name: 
# Python Version: 3.6.3
# Date Started - Date Finished: 01/16/2018
# Description: 	Write a program which asks the user for a student's grade as a percent, and then returns their letter grade.
#				NOTE: You must VALIDATE the INPUT (so make sure the number is between 0 - 100 ... for any other number, say  
#				"ERROR" and ask for another number)
#				A is 90% or above
# 				B is between 80% and 90%
#				C is between 70% and 80%
#				D is between 60% and 70%
#				F is under 60%

# ask the user to enter grade as a percentage
percent = float(input('Please enter the grade percent: '))

# validate the user input
# ...make sure the percentage is between 0 - 100
if percent < 0 or percent > 100:
	print('Invalid percentage entered, must be between 0-100')
	percent = float(input('Please enter the grade percentage: '))
	
# show the correct letter grade based on the percentage
if percent >= 90 and percent <= 100:
	print('The letter grade is A')
elif percent >=80:
	print('The letter grade is B')
elif percent >=70:
	print('The letter grade is C')
elif percent >=60:
	print('The letter grade is D')
else:
	print('The letter grade is F')
	

'''
C:\python>python3 p10.py
Please enter the grade percent: 95
The letter grade is A

C:\python>python3 p10.py
Please enter the grade percent: 35
The letter grade is F

C:\python>python3 p10.py
Please enter the grade percent: 95
The letter grade is A

C:\python>python3 p10.py
Please enter the grade percent: 85
The letter grade is B

C:\python>python3 p10.py
Please enter the grade percent: 75
The letter grade is C

C:\python>python3 p10.py
Please enter the grade percent: 65
The letter grade is D

C:\python>python3 p10.py
Please enter the grade percent: 55
The letter grade is F

C:\python>python3 p10.py
Please enter the grade percent: 110
Invalid percentage entered, must be between 0-100
Please enter the grade percentage:
'''
