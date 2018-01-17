# Program name: p0.py
# Your Name: Alex Stoykov
# Python Version: 3.4.4
# Date Started - Date Finished: 08/31/17 
# Description:
''' COPY/PASTE DESCRIPTION FROM THE ASSIGNMENT:
Write a program which computes the sum and product of two numbers entered by the user.
Algorithm:
1) Ask the user to enter two numbers.
2) store those two numbers in 2 variables, num1, num2.
3) make two new variables sum = num1+ num2, and product = num1*num2
4) Then, output the sum and product of to the user.

Sample Program Run:
Please enter number 1: 10
Please enter number 2: 20
The sum of 10 and 20 is 30
The product of 10 and 20 is 200
'''

# THE ABOVE COMMENTS DOCUMENT YOUR CODE AND ARE WORTH (30% of  your grade)


# COMMENT
# comments are not considered part of your code
# comments are just explanation of your code

# OUTPUT
print ("Hello!") # print() is how we show "OUTPUT"
# OUTPUT is information that comes OUT of the program
# anything in quotes " " (or single quotes ' ') will be shown exactly as is
# anything in quotes "" (or single quotes ' ') is a STRING = text

# DIFFERENT TYPES OF INFORMATION
# A.K.A. "DATA TYPES"
# TEXT = STRING  = anything in " "
# NUMBERS: Whole Numbers (Integers), Decimal Numbers (Float)

# WE STORE THE INFORMATION USING "VARIABLES"
# VARIABLES = words we make up, which refer to some place in memory, where information is stored
# RULES FOR VARIABLE NAMES:
# 1) Can't start with a number
# 2) No spaces in variable names
# 3) No special characters: !@#$%^&* ... only _ is allowed
# 4) Don't use reserved words such as: print, input, int, float as variable names
# 5) Use meaningful variable names

#VARIABLE NAME         INFORMATION STORED IN THE VARIABLE
name             =     "Alex S."   # Text/STRING
age              =       19        # Whole number (INTEGER), no decimal
weight           =       175.567   # Decimal number (FLOAT)
#                ^ASSIGNMENT OPERATOR

# STRING CONCATENATION
first = "Alex"
last = "Stoykov"
first_last = first + last # CONCATENATION = combine two or more strings into one bigger string using +
print('first_last=', first_last)

first = "Alex"
last = 3
first_last = first + str(last) # CONCATENATION = combine two or more strings into one bigger string using +
#                    ^^^^^^^^^ CAST the variable 'last' into integer
# CASTING = temporarily force a variable to change its data type
print('first_last=', first_last)

first = "3"
last = 3
first_last = first + str(last) # two strings, so it concatenates
print('first_last=', first_last) # 33

# NOT STRING CONCATENATION
first = "3"
last = 3
first_last = int(first) + last # two integers, so it does the math
print('first_last=', first_last) # 6

# FORMATTING YOUR OUTPUT
print("name=", name, "age=", age, "weight=",weight)
print('name=', name, 'age=', age, 'weight=',weight)
print('name= %s' %name, 'age= %i' %age, 'weight= %f' %weight)
# %s = string; %i = integer; %f = float
print('name= %s' %name, 'age= %i' %age, 'weight= %.2f' %weight) #*SAME*
# %.2f = a float rounded to 2 decimal digits
print('name= %s age= %i weight= %.2f' %(name,age,weight)  )  #*SAME*
print("name= " + str(name) + " age= " + str(age) + " weight= " + str(weight) )

# INPUT = Information goes IN the program
# input() can be: string, int, float
# default/String INPUT
name = input("Please enter a new name:") # input() is for a STRING
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^PROMPT = tell the user what to enter
print ("name=",        name) # OUTPUT a variable
#      ^^^^^^LABEL     ^^^^CONTENT OF THE VARIABLE name

# Integer INPUT
# Input cannot be: string, float
# int(input()) can only be INTEGER
age = int(input("Please enter a new age:"))
print("age = ", age) # show myself the content that was entered into variable age

# Float INPUT
# Input cannot be: STRING
# float(input()) can  be: integer, float 
weight = float(input("Please enter a new weight:"))
print("weight = ", weight) # show myself the content that was entered into variable age

#p2 Hint

print("************************************************")
print("")
print("            C C C                 S S S")
print("          C       C              S     S")
print("         C                      S")
# do the rest yourself

# p5 Hint
num1 = int(input("Please enter num1:"))
num2 = int(input("Please enter num2:"))
Sum = num1+num2
print("the sum of", num1, "+", num2, "=", Sum)

''' MULTILINE COMMENT TO SHOW ME HOW YOUR PROGRAM RAN/TESTED (30% of grade)
================== RESTART: /Users/anonymous/Desktop/p0.py ==================
Hello!
first_last= AlexStoykov
first_last= Alex3
first_last= 33
first_last= 6
name= Alex S. age= 19 weight= 175.567
name= Alex S. age= 19 weight= 175.567
name= Alex S. age= 19 weight= 175.567000
name= Alex S. age= 19 weight= 175.57
name= Alex S. age= 19 weight= 175.57
name= Alex S. age= 19 weight= 175.567
Please enter a new name:1
name= 1
Please enter a new age:1
age =  1
Please enter a new weight:1
weight =  1.0
************************************************

            C C C                 S S S
          C       C              S     S
         C                      S
Please enter num1:10
Please enter num2:20
the sum of 10 + 20 = 30
>>> 
'''
