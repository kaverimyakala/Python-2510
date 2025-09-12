# Strings
# valid strings are:

s1 = "data"
s2 = 'data'
s3 = """data"""   #multiline strings  can only used triple quotes 
s4 = '''data'''

print(s1)
print(s2)
print(s3)
print(s4)

print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))  

m1s = """this is very big line of string
more line 
more line """ 
print(m1s)

#inside a string 

question = "how are you"
answer = "i'm fine"  # ' used inside the quotes should use double quotes(" ' ")
print(answer)

answer = 'doing "great"' # if you want to use double quotes inside and enclosed with single quotes
print(answer)

# if you want to use both single and doubles quotes inside a string need enclosed with tripple quotes

answer = """i'm fine doing "great" """
print(answer)

#INDEXING 
# Python allows you to access each character in a string using am index number
# index start from 0
# indexing goes in both positive and negative directions too

# text = "Python"
# 0   1   2   3  4  5
# p   y   t   h  o  n
# -6 -5  -4  -3 -2 -1  

text = "Python"
print(text)   # it will print whole string input 

# if you want to print specific thing indexing will use 

# Indexing : accessing characters 

print(text[0])  # this will print first letter 
print(text[1])  # this will print  second   so on.... postive direction 
print(text[2])  
print(text[3])
print(text[4])
print(text[-1])  # when it comes to negative index it will pring last letter  so...on  negative direction  
print(text[-5]) 

# print(text(10)) #str' object is not callable  so this index is  out of range bec' input is only upto 6
# if you give negative is also it will givw out of range

# if you want to print whole text each chracter separatly the above method we can use but that was time taking 
# so with in short time we can use loops 

# using loop  to access

for character in text:
    print(character)

# Note : we have a predefind function len ()
# len() return the number of items in an object 

print("length is:",len(text))

# example using  list

list_data = ["dell","lenova","mac","apple"]
print("brands count is:",len(list_data)) 

#note: in python space is also character 
brand = "apple   " 
print("length is:",len(brand))

# len does not work with numbers
# num 100
# print("length is",len(num))  # Typeerror : object of type 'int' has no len()

# slicing 
# is means cutting a substring from the original string using index to access range of characters ina string 
# string[start:stop:step]            in range(start:stop:step)

text = "python"
print(text[0])  # access using index

print (text[0:3]) #start at 0: stop at 3:  step is default 1  so it will give uptp 2index 3 is excluded

print(text[0:]) #start at 0 :  but no stop we given means it will print entire thing 

print(text[:]) #  nothing has given means it will print entire thing

print(text[2:5]) # start at indext 2 and stop at 5 

print(text[:4]) #start nothing as given so it will print till 4 th index from start point 

#Back word 
# Negative slicing (backword)

text = "python"
print((text[-1]))

print(text[-1:])  # last index of text
print(text[-4:-1]) #  its worng direction 
print(text[-4:-1:1]) # its wrong direction 
print(text[-4:-6:-1]) # starts at -4 so it will include till -5 excluded -6 stop point 
print(text[1:4:-1])  # empty beacause direction was -1  but start point is 1 so its not possible dirction 
print(text[::-1])  # it will print reverse string beacause -1 is back direction start point  and stop point nothing has given it will print entire string

# without using  indexing  we can also use reverse string throuh loops 
text = "python"
reversed_text = ""
for character in text:
    reversed_text = character + reversed_text
print("reversed text",reversed_text)

#string immutability once a string is created,it cannot be changed 

# reassigning
text = "hello"
print(text)
text = "hi"
print(text) 

# string immutability
#text = "hello"
#print(text) 
# modify hello to Hello
#text[0] = "H"  #TypeError: 'str' object does not support item assignment

s1 = "Hello"
s2 = "Good Morning"
print(s1+s2) 

name = "kavya"
age = 20
print("my age is",age)
print(f"My age is",{age})
print("my age is",+age)
print("my age is"+ str(age))

#string formatting 
#string repetition multiply the string using operator 

text = "Ha"
laugh = "hahahahahaha"
print(laugh)
laugh_hard = text*10
print(laugh_hard)

#string methods
#string class providers multiple methods to work string related operations

text = "ha"
print(dir(text)) 

#simulate gmail functionality using strings

user_given_email = input("enter your mailID:")
format_email = user_given_email.lower()+"@gmail.com"
print("user given ID:",user_given_email)
print("Gmail Autoformat ID:",format_email)

#simulating PAN functionality using condition

user_given_pan = input("enter your input PAN ID:") 
if user_given_pan.isalnum():
    format_pan = user_given_pan.upper()
    print("user given ID:",user_given_pan)
    print("pan Autoformat ID:",format_pan)
else:
    print("user given PAN is invalid:"+user_given_pan)

#Check for substring
#simulate mail id verifying name@gmail.com 

user_given_email = input("enter your mailID:")
if user_given_email.find("@")!=-1:
    print("valid email")
else:
    print("invalid email")

#obave can be achieved using operator also
user_given_email = input("enter your email ID:")
if "@" in user_given_email:
    print("valid email")
else:
    print("invalid")

# redirect call based on given isd code
phone_number = input("enter you phone number:")
if phone_number.startswith("+91"):
    print("call connected to INDIA")
elif phone_number.startswith("+86"):
    print("call connected to china")
elif phone_number.startswith("+33"):
    print("call connected to fRANCE")
else:
    print("isd available only to india,china,france")

# check if email synchronisation is possible or not 

user_given_email = input("enter your email id:")
source_email = input("enter your destination email id to sync:")
if source_email.endswith("gmail.com")and user_given_email.endswith("gmail.com"):
    print("synchronizing")
else:
    print("Both email should be from same providers")

#simulate gmail functionality remove space from input

user_given_email = input("enter your mailID:")
format_email = user_given_email.strip()
print("user given ID:"+user_given_email)
print("Gmail Autoformat ID:"+format_email)

# read data from csv file
# sample data taken from a csv file 

#original data
csv_line = "john,Hyd,20,john@gmail.com,developer"
#original data
print("original line:",csv_line)
#parsed data
parsed_field = csv_line.split(",")
print("parsed data:",parsed_field)

#Access name and role 
print("Name:",parsed_field[0])
print("Role:",parsed_field[4]) 

# vs code find and replace /otp template /order/id template 

email_template = "hello user, your order #{order_id} has been shipped"

order_id = "OD-ID-9090"

#replacing placeholder with values
personalized_email = email_template.replace("{order_id}",order_id)

print(personalized_email)
