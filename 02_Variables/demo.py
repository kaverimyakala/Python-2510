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