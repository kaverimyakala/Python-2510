#Variables  

student_name = "Kaveri"
student_age = 21
student_cgpa = 7.5
student_passed = True
student_roll_no = 21   

student1_marks = [20,20,78]
student2_marks = [39,49,20]

print(student_name)
print(student_age)
print(student_cgpa)
print(student_passed)
print(student_roll_no) 

print(id(student_name))
print(id(student_age))
print(id(student_cgpa))
print(id(student_passed))   #id() is used memory location of variable 
print(id(student_roll_no))    # it will print the same address for age and roll no why means it may be same data type   

print(id(student1_marks))
print(id(student2_marks))   #it will not print the same address bec' it was mutual data 

#To know about data type what type of data we print use 'type()' to get data type  


print(type(student_name))
print(type(student_age))
print(type(student_cgpa))
print(type(student_passed))
print(type(student_roll_no))
print(type(student1_marks))  

#Any object of a Class is Variable 

data_one = "Good"
data_two = " Morning"
print(data_one + data_two)  #Concatenation : joining multiple strings together using '+' Operator

num1 = 20
num2 = 30
print(num1 + num2) # Addition Perform mathmatical addition operation 

# print (num1 + data_two) #unsupported operand type(s) for +: 'int' and 'str' it can not do string and integer both should be intg or str

name = "kaveri"
age = 22
cgpa = 7.5
print(f"my name is {name} my age is {age} and my cgpa is {cgpa}" ) # INTERPOLATION IS replacing placeholders with actual values

x = 10 
y = 20 
z = 30
print(x)
print(y)
print(z)

x,y,z = 10,20,30
print(x,y,z)

x=y=z = 10
print(x,y,z)

x = 10
y = 20
z = 30
print(x,y,z)

'''x,y,z = 10,20,30,40
print(x,y,z) #too many values to unpack (expected 3) there should be LHS == RHS'''

n1 = 3
n2 = 2 
print(f"sum of n1 & n2 is {n1+n2}")
print(f"difference of n1 & n2 is {n1-n2}")
print(f"product of n1 & n2 is {n1*n2}")
print(f"division of n1 & n2 is {n1/n2}")
print(f"modulus of n1 & n2 is {n1%n2}")
print(f"floor division of n1 & n2 is {n1//n2}")

x = 5
x*=5   #with compound assignment
print(id(x)) # x=5  *5 = 25

x = 10
x+= 5 #x = 10 +5 =15
print(id(x))

x = 10
x = x + 5  # without compound assignment 
print(id(x))  # x = 10 + 5 = 15

# Comparision operators 
 
n1 = 2
n2 = 4
print(n1 == n2)
print(n2 == n1)
print(n1 != n2)
print(n2 != n1)
print(n1 > n2)
print(n2 > n1)
print(n1 < n2)
print(n2 < n1)
print(n1 >= n2)
print(num1 >= n2)
print(n1 <= n2)
print(n2 <= n1)



# Logical Operations

a = 2
b = 4
c = 7
d = 9
resultAND = a > b and b < d  # F AND T SO F
print(resultAND)

resultAND = a < b and b < d # T AND T SO T   AND operation it returns true ,when both conditions T
print(resultAND)

resultOR = a > b or b < d  # F AND T so T 
print(resultOR)   # OR operation it returns true when at least one condition T

resultOR = c > b or b > d # T AND F so by following rule 'OR' we get T  
print(not resultOR)    # SO, NOT Opperation says IF true means false, false means true so ANSWER WAS False.

resultAND = (a > b) and not (b < d)
print(resultAND)  # not was applying for only 2nd condition 


# Membership Operations (in/NOT in)

# List is a Sequence data type

list_nums = [20,30,40,50,60]
is_present = 10  in list_nums
print(is_present)

list_nums = [40,70,30,59]
is_present = 59 in list_nums
print(is_present)

# String is also sequence Data  Type

Text = "Apple"
is_present = "A" in Text
print(is_present)

Text = "Apple"
is_present = "A" not in Text
print(is_present)

#Identity Operators 

n1 = 10 
n2 = 10
n3 = 10.0
print(n1 == n2) 
# T if both variables are pointing to same address
print(n1 is n3)  # So its false address was not same
print(n1 is not n3) # T because is not same address

#Note : Numbers are immutable(not changeable) data type
#List : Numbers are mutable(Changeable) data type 

l1 = [10,20,30]
l2 = [10,20,30]
print(l1 == l2) # T bec it will compare values 
print(l1 is l2) # it will print F bec ' both list address will not have same
print(l1 is not l2)

# printing ID's of data

print(id(l1))
print(id(l2)) # so both address are different 

print(id(n1))
print(id(n2))
print(id(n3))

print(id(l1[0]))
print(id(l2[0])) # idivualy it will print same address nut mutually it wiil not

#Bitwise Operators 

a = 10
b = 7
print(a & b)
print(a | b) 

# Data TYpes 

brand = "Biba"
product = "Women Blue & White Printed Kurta with Crop Palazzos"
rating = 4.1
price = 1150

print(type(brand))
print(type(product))
print(type(rating))
print(type(price))

com_num = 2 + 3j
print(type(com_num)) 

list_nums = [10,20,30,40]
print(type(list_nums))


tuple_nums = (10,20,30,40)
print(type(tuple_nums))


set_nums = {10,20,30,40}
print(type(set_nums))


dic_data = {"name":"kaveri","age": 21}
print(type(dic_data))

x = None
print(type(x))      
# ALL these are predefind data types 

# Created own datatypes are below

class student:
    pass 
lync_student = student()
print(type(lync_student))
print(id(lync_student))