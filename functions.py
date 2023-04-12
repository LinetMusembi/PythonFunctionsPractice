# python functions
# A function is a group of statements that is used to perform a particular task.
# functions are reusable

# Exercise1
# Write a program to create a function that takes two arguments, name and age and 
# print their value.

def sum(name,age):
    age = 2023-age
    print(f"Hello,my name is {name} and i am {age} years old")

# Exercise2
# Create a function with variable length of arguments.
# Variable length of arguments is used when you do not know the number of 
# argumnents in advance.

# Types of abitrary arguments
# a).args(*)

# NB....This function will work but it limits the number of arguments to use
# so it will not be efficient if we had many arguments.
def percentage(sub1,sub2,sub3):
    avg = (sub1+sub2+sub3)/3
    print(avg)

# Better option:
def percentages(*args):
    sum = 0
    for i in args:
        sum = sum + i
        avg = sum/len(args)
        print(avg)

# b).kwargs(**kwargs)
# Allows you to pass multiple keyword arguments to a function
def percentage(**kwargs):
    sum = 0
    for sub in kwargs:
        sub_name = sub
        sub_marks = kwargs[sub]
        print(sub_name, "=", sub_marks)

# Exercise3
# Return multiple values from a function

# Write a program to create function calculation() such that it can 
# accept two variables and calculate addition and subtraction. Also, it must return 
# both addition and subtraction in a single return call.

# NB...in Python to return multiple function,use a comma to separete them.

def calculation(a,b):
    addition = a +b
    subtraction = a -b
    return addition,subtraction

res = calculation(40,10)
print(res)


# Exercise4
# Create a function with a default argument

# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 
# 9000 to salary

# NB...Default arguments take the default value during the function call if we 
# do not pass them.

def show_employee(name,salary=9000):
    print("Name:",name,"salary",salary)

# Exercise5
# Create a recursive function

# Write a program to create a recursive function to calculate the sum of 
# numbers from 0 to 10.
# A recursive function is a function that calls itself again and again.

def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0
res = addition(10)
print(res)

# Exercise6
# Assign a different name to function and call it through the new name.
# Below is the function display_student(name, age). Assign a new name show_student
# (name, age) to it and call it using the new name.

def display_student(name, age):
    print(name, age)

display_student("Lynet", 26)


showStudent = display_student
showStudent("Lynet", 26)

# Types of argument functions
# 1.Default Arguments

# Let’s define a function student() with four arguments name, age, grade, and school. 
# In this function, grade and school are default arguments with default values.

def student(name,age,grade = "one",school="Mountain view"):
    print("student detail:",name,age,grade,school)

# 2.Keyword Arguments
# Here,values get assigned to the arguments according to their position.
# NB...So we must pass values in the order as written in the argument.

def interest(name,school):
    print(f"I do not know{name} well,but she is in {school}High school")








