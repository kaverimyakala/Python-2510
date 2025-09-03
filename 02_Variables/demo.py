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
