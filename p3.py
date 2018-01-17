# Program name: p3.py
# Your Name: 
# Python Version: 3.6.3
# 01/07/2018
# Description:  Program to take input in Python
#               Type up the Example input.py program, including the comments (in RED), 
#               and get it working.

name = input ("Please enter Your Name: ") # this is a string
weightLbs = float(input ("Please enter Your weight in lbs: ")) # a float
age = int (input ("Please enter your age (whole number): "  )) # an integer
weightKg= weightLbs*0.453592
title = "Human"

print ("Hello", title, name, "your weight is")
print (weightLbs, "lbs")
print ("which equals = %.2f" %weightKg, end=' ') #end ="" prints new line
print ("kilograms ")

'''
C:\python\python3 p3.py
Please enter Your Name: Grigor Dimitrov
Please enter Your weight in lbs: 179
Please enter your age (whole number): 26
Hello Human Grigor Dimitrov your weight is
179.0 lbs
which equals = 81.19 kilograms
'''
