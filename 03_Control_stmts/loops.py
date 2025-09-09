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



