# Program name: p06.py
# Your Name: 
# Python Version: 3.6.3
# Date Started - Date Finished: 01/16/2018
# Description: 	Write a program to compute a person's height.
# 				INPUT: User will enter two whole numbers: feet and inches.
# 				OUTPUT: Values input & total in inches.

# ask the user for height, feet, and inches
feet = float(input('Please enter the number of feet: '))

inches = float(input('Please enter the number of inches: '))

# calculate the total inches
total_inches = feet * 12 + inches
# show the results
print ( '%.0f feet %.0f inch(es) = %.0f inches'
		%(feet,	inches, total_inches)
		)


'''
Please enter the number of feet: 4
Please enter the number of feet: 10
4 feet 10 inch(es) = 58 inches
'''