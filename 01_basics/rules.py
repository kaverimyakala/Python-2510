#Python is a programming language.
#syntax/rules

# means comment ,Python will nor run this line

a = 2002
print(a) # it will print what will gave as input

#greet = good morning  invalid syntax 
#print(greet) it will give syntax error
# collextion of characters is calles as string in python
#  rules - Strings should be enclosed in '' or ""

greet = "Good Morning"
print(greet)

#IN PYTHON WE HAVE 35 KEYWORDS
#KEYWORDS + SYNTAX = PROGRAM/APPLICATION
# Keywords get all the keywords

import keyword
print(keyword.kwlist) # it will run all keywords

#IDENTIFIERS
# As a Python is a name used to Identify variables,functions,class,object, methods,etc.
# RULES
# LETTERS(a_z,A_Z)
# Digits(0_1) and ONLY UNDERSCORES
# STart with letters,underscores BUT NOT WITH digits(0_1),KEYWORD
# cant not be case sensitive  

myname = "Kaveri"
print(myname) 

'''2_myname = "Myakala" # Invalid SYntax Identifier can not start with a digit 
print(2_myname) # SYntax error'''

_myname = "Myakala"
print(_myname)

'''class = 9 #syntax error  bec Identifier can not be a keyword
print(class) # invalid syntax'''

