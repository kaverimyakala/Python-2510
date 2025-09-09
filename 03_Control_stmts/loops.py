#while 
#syntax

# while condition
# code to repeat 

count = 1                # intially given count 1 so 
while count <= 5:        # while condtion is to say repeat  so repeat the count <=5 
    print(count)         # print count means its prints only one  
    count += 1           # now count is 1 so next it increment 1 so now count was 2 ,It repeats until it reachaes condition


chocolates = 5 
while chocolates > 0:
    print(chocolates)
    chocolates -= 1
print("no chocolate left!")


# real time example 

atm_correct_pin = 1234
user_given_pin = 0

while user_given_pin != atm_correct_pin:
    user_given_pin = int(input("enter pin: "))
print("you can withdraw")

#infinite loop
'''count = 1
while True:
    print(count)
    count += 1  '''


# For loop 
#syntax
# for element in sequence 

text = "python is a general purpose  programming" 
for char in text:
    print(char)


num = 10 
print(dir(num)) # used to list all the valid attributes and functionlaties 

text = "always"
print(dir(text)) 

#for loop : repeat block of code , if you know number of iteration in advance 

#range used to generate a sequence of numbers

# range()

for num in range(10):
    print("Hi")

for num in range (1,6):
    print(num)

for num in range (1,6,1):
    print(num)

for num in range (2,6,2):
    print(num)

for num in range (2,10,2):
    print(num)

'''for num in range (2,5,8,2): # range expected at most 3 arguments, got 4 .so,it will not accept more then 3 arguments.
    print(num)'''

# reverse  

for num in range (10,1,-1):   #so stop always excluded : start always included 
    print(num)


for num in range (10,1,-2):
    print(num)

# loop with conditions 
print("printing even nums from 1 to 20 ")

num = 2
while num <= 20:
    print(num)
    num += 2 

for num in range (2,21,2):
    print(num)

course_list = ["Python","cloud","devops","ai"]
for course in course_list:
    print(course)


# Nested loop

for i in range (1,4):
    for j in range (1,4):
        print(f"{i} x {j} = {i * j}")
    print("-----") 

i = 1
while i < 4:
    j = 1
    while j < 4:
        print(f"{i} x {j} = {i * j}")
        j += 1
    print("---")
    i += 1  

#Branching statements 
# break exit the loop entirely

for num in range(5):
    if num == 3:
        break  # so it stop the loop when it comes 3 
    print(num)

for num in range(5):
    if num == 3:
        continue # skip the current iteration 
    print(num)

for num in range(5):
    if num == 3:
        pass  
    print(num) # does nothing 

