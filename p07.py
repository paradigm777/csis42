# Program name: p07.py
# Your Name: David Flynn
# Python Version: 3.6.3
# Date Started - Date Finished: 01/16/2018
# Description: 	Write a program to compute the circumference and area of a circle.
# 				The user will input the radius of the circle.
# 				Output will show the circumference and area of the circle with that radius.
# 				The answers should round to the nearest tenth.

# define variable PI
PI = 3.1415

# ask the user to enter a radius
radius = float(input('What is the radius (in inches) of the circle you want to draw? '))

# calculate the circle area
circle_area = PI * radius * radius

#calculate the circumference
circumference = 2 * PI * radius

# show results exactly as shown in the assignment
print('A circle with radius %.0f inches has' %(radius))
print('circumference: %.1f inches' %(circumference))
print('area: %.1f inches' %(circle_area))

'''
What is the radius (in inches) of the circle you want to draw? 12
A circle with radius 12 inches has
circumference: 75.4 inches
area: 452.4 inches
'''

