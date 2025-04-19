############################################################
# Part 1: Learning Exercises 
# input() and and .format()

# name = input("what is thy name, sire?")
# msg = input ("what is thy command")
# print(name + "says" + msg)
# color = input("what is your favourite color?")








# Exercise 1: Using input() for Text
# Write a program to ask the user for their favorite color and display it.
# Example: If the user enters "blue", the program should display
# "Your favorite color is blue."
# color = input("What is your favorite color? ")
# print("Your favorite color is " + color + ".")




#------------------------------------------------------------
# Exercise 2: Understanding input() Behavior
# Write a program to ask the user for their age and display it.
# Example: If the user enters "15", display "Your age is 15."
# Note: Treat the input as a string for now.
# age = input("Enter your age: ")
# print("Your age is " + age + ".")




#------------------------------------------------------------
# Exercise 3: Comparing String Formatting Methods
# Write a program to ask the user for their name and age and display it
# in three different ways. Example: Input name = "John", age = 15
# name = input("Enter your name: ")
# age = input("Enter your age: ")

# # Using + concatenation
# print("Concatenation: " + name + " is " + age + " years old.")

# # Using .format()
# print("Using .format(): {} is {} years old.".format(name, age))

# # Using f-strings
# print(f"Using f-strings: {name} is {age} years old.")
# name = "Edmund"
# age = 15 
# print("my name is",name)
# print("my name is {}. I am {} years old.".format(name, age))




#------------------------------------------------------------
# Exercise 4: Formatting a Message with .format()
# Write a program to display a sentence about favorite subjects.
# Example: Input subject = "Math", reason = "exciting"
# subject = input("Enter your favorite subject: ")
# reason = input("Why do you like it? ")
# print("I like {} because it is {}.".format(subject, reason))
# subject = input("what is your favourite subject ")
# reason = input("why do you like it? ")
# print("i like {} because it is {}.".format(subject, reason))





#------------------------------------------------------------
# Exercise 5: Comparing .format() and f-strings for a Calculation
# Write a program to calculate the sum of two numbers and format the
# output in two ways: using .format() and f-strings.
# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# num1 = int(num1)
# num2 = int(num2)1
# result = num1 + num2

# # Using .format()
# print("Using .format(): The sum of {} and {} is {}.".format(num1, num2, result))

# # Using f-strings
# print(f"Using f-strings: The sum of {num1} and {num2} is {result}.")


# name = Input("what is thy name sire")
# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# num1 = int(num1)
# num2 = int(num2)
# result = num1 + num2
# print(f"Using f-strings: The sum of {num1} and {num2} is {result}. ")





###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 6: Greeting with .format()
# Write a program to ask the user for their name and print a greeting
# using .format(). Example:
# Input: name = "Alice"
# Output: "Hello, Alice! Have a great day!"

# Input: name = "Ranen"
# Output: "Hello, Ranen! Have a great day!"
# name = input("what is your name ")
# print(f"hello {name} have a great day ")



#------------------------------------------------------------
# Exercise 7: Adding Two Numbers with .format()
# Write a program to ask the user for two numbers, convert them to integers,
# add them, and display the result using .format(). Example:
# Input: 5, 3
# Output: "The sum of 5 and 3 is 8."


# '''
# # Part 3. Challenge Exercises
# # Exercise 1: Greeting with .format()
# # Write a program to ask the user for their first and last name.
# # Use .format() to display a full greeting message.
 
# Example:
# # Input: first_name = "John", last_name = "Doe"
# # Output: "Hello, John Doe! Welcome to Python programming."
 
# # You must follow the exact sentence format above to complete this exercise.
# '''
# fname = "ranen", lname = "yeo"
# fname = input("what is your first name? ")
# lname = input("what is your last name? ")
# print(f"hello {fname} {lname} Welcome to Python programming")




#------------------------------------------------------------
# Exercise 8: Area of a Circle with .format()
# Write a program to ask the user for the radius of a circle, convert it to
# a float, calculate the area using the formula (area = 3.14 * r^2), and
# display the result using .format(). Example:
# Input: radius = 7
# Output: "The area of the circle is 153.86."





#------------------------------------------------------------
# Exercise 9: Describing a Favorite Activity
# Write a program that asks the user for their favorite hobby and explains
# why they like it. Format the output using .format().
# Example: hobby = "reading", reason = "relaxing"
hobby = input("what is your hobby? ")
reason = input("what is the reason you like it? ")
print(f"i like {hobby} because its {reason} ")

"I like reading, because it is relaxing"





#------------------------------------------------------------