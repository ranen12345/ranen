###################################################
# Part 1: Learning Exercises

# Exercise 1: Variables and Assignments
# Assign values to variables and calculate their sum.
# Example: Assign 10 to a and 20 to b. Calculate their sum.
a = 10
b = 20
sum_value = a + b
print("Sum of a and b is:", sum_value)




#------------------------------------------------------------
# Exercise 2: Adding Comments
# Add a single-line and a multi-line comment in this code.
# Example: Add comments to explain what the code does.
# Single-line comment
"""
This is a multi-line comment.
It explains the code in detail.
"""
print("Comments explain your code.")




#------------------------------------------------------------
# Exercise 3: String Concatenation
# Combine two strings to make a greeting.
# Example: Assign "Hello" to greeting and "John" to name.
# Combine them to display: "Hello John".
greeting = "Hello"
name = "John"
message = greeting + " " + name
print(message)




#------------------------------------------------------------
# Exercise 4: String Repetition
# Repeat a phrase multiple times to create a pattern.
# Example: Print the phrase "Python is fun! " three times.
phrase = "Python is fun! "
print(phrase * 3)




#------------------------------------------------------------
# Exercise 5: Combining Variables
# Use variables to create a descriptive sentence.
# Example: Assign "Python" to language and "awesome" to
# adjective. Combine them to display: "Learning Python is
# awesome!"
language = "Python"
adjective = "awesome"
print("Learning " + language + " is " + adjective + "!")

# print("Hello, world")
# x=10
# y=20
# z= x+y
# print("z")
essay=""" This is a story 
of a cat and a dog 
sitting inder the papaya tree
and drinking milk
"""
greeting = "Hola"
name ="Ranen"
message = greeting + "" +name
print(message)
# option 2 : to use comma (this only works inside a print())
print('ni hao ', 'axl')
print('go!'* 5)

###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 1: Variables and Operations
# Subtract two numbers stored in variables. Try changing them.
# Example: Assign 15 to x and 5 to y. Calculate x - y.
a = 4
b = 8
sum_value = b - a
print(sum_value)



#------------------------------------------------------------
# Exercise 2: Adding Comments to Code
# Add comments to explain each line in this code.
# Example: Store first and last names, combine them, and
# print a greeting.

first_name = "Alice"  # Store first name
last_name = "Tan"     # Store last name 
full_name = first_name + " " + last_name  # concatenation, joining sentences together
print("Welcome, " + full_name + "!")  





#------------------------------------------------------------
# Exercise 3: String Concatenation
# Combine variables into a full sentence.
# Example: Assign "sunny" to weather and "picnic" to activity.
# Combine them to display: "It is a sunny day for a picnic."
weather = "sunny"

weather="sunny"
activity="picnic"
print("it is a ",weather ,"day for a" ,activity)





#------------------------------------------------------------
# Exercise 4: String Repetition
# Use repetition to create a patterned message.
# Example: Print "Go! " five times to display: "Go! Go! Go!
# Go! Go!"
print ("Go!"*5)
length=12
width=8
print(2*(length+width))
name="alice"
hobby="reading"
print(name+ ' ' + hobby)
############################################################
# Part 1: Learning Exercises 
# input() and and .format()

# Exercise 1: Using input() for Text
# Write a program to ask the user for their favorite color and display it.
# Example: If the user enters "blue", the program should display
# "Your favorite color is blue."
color = input("What is your favorite color? ")
print("Your favorite color is " + color + ".")




#------------------------------------------------------------
# Exercise 2: Understanding input() Behavior
# Write a program to ask the user for their age and display it.
# Example: If the user enters "15", display "Your age is 15."
# Note: Treat the input as a string for now.
age = input("Enter your age: ")
print("Your age is " + age + ".")




#------------------------------------------------------------
# Exercise 3: Comparing String Formatting Methods
# Write a program to ask the user for their name and age and display it
# in three different ways. Example: Input name = "John", age = 15
name = input("Enter your name: ")
age = input("Enter your age: ")

# Using + concatenation
print("Concatenation: " + name + " is " + age + " years old.")

# Using .format()
print("Using .format(): {} is {} years old.".format(name, age))

# Using f-strings
print(f"Using f-strings: {name} is {age} years old.")




#------------------------------------------------------------
# Exercise 4: Formatting a Message with .format()
# Write a program to display a sentence about favorite subjects.
# Example: Input subject = "Math", reason = "exciting"
subject = input("Enter your favorite subject: ")
reason = input("Why do you like it? ")
print("I like {} because it is {}.".format(subject, reason))




#------------------------------------------------------------
# Exercise 5: Comparing .format() and f-strings for a Calculation
# Write a program to calculate the sum of two numbers and format the
# output in two ways: using .format() and f-strings.
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num1 = int(num1)
num2 = int(num2)
result = num1 + num2

# Using .format()
print("Using .format(): The sum of {} and {} is {}.".format(num1, num2, result))

# Using f-strings
print(f"Using f-strings: The sum of {num1} and {num2} is {result}.")


