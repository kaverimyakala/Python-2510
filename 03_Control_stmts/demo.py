# Conditional Statements 
#if syntax 
#         condition      

if True:
    print("Correct Identation")
    print("Correct")

if 5 > 2:
    print("valid condition")

if 5 < 2:
    print("valid condition")
else:
    print("invalid condition")


# Voting APP

age = 17
if age >= 18:
    print("Yes, You are eligible to vote")
else:
    print("No, You are not eligible to vote")

# input() -> for taking input from user

value = input("enter the value")
print(value)
print(type(value)) 

# dynamic voting app
'''age = input("enter age: ")
if age >= 18:         #not supported between instances of 'str' and 'int'
    print("Yes, You are eligible to vote")
else:
    print("No, You are not eligible to vote")'''

age = int(input("enter age: "))        # here, we did TYPE CASTING (str converted to int)
if age >= 18:         
    print("Yes, You are eligible to vote")
else:
    print("No, You are not eligible to vote")

# Ternary Operator
# value_if_true if condition else value_if_false 

age = int(input("enter age: "))
status = "Yes, You are eligible to vote" if age >= 18 else "No, You are not eligible to vote"
print(status)

# elif ladder - multiple conditions

student_marks = int(input("enter the marks: "))
if student_marks >= 90:
    print("GRADE A")
elif student_marks >= 75:
    print("GRADE B")
elif student_marks >= 65:
    print("GRADE C")
elif student_marks >= 35:
    print("PASS")
else:
    print("FAIL")

# Match case (switch case in java)

choice = int(input("enter your choice (1-5): "))
match choice:
    case 1:
        print("C")
    case 2:
        print("#c")
    case 3:
        print("Python")
    case 4:
        print("Java")
    case 5:
        print("Devops")
    case _:
        print("Select only choice between (1-5)")


