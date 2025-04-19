# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: Converting to Uppercase
# # Write a program to convert a string to uppercase.
# # Example: Input = "hello", Output = "HELLO".
# word = "hello"
# uppercase_word = word.upper()  # Convert to uppercase
# print("Uppercase: {}".format(uppercase_word))




# #------------------------------------------------------------
# # Exercise 2: Converting to Lowercase
# # Write a program to convert a string to lowercase.
# # Example: Input = "HELLO", Output = "hello".
# word = "HELLO"
# lowercase_word = word.lower()  # Convert to lowercase
# print("Lowercase: {}".format(lowercase_word))




# #------------------------------------------------------------
# # Exercise 3: Checking if a String is Uppercase
# # Write a program to check if a string is fully uppercase.
# # Example: Input = "HELLO", Output = True.
# word = "HELLO"
# is_upper = word.isupper()  # Check if uppercase
# print("Is '{}' uppercase? {}".format(word, is_upper))




# #------------------------------------------------------------
# # Exercise 4: Checking if a String is Lowercase
# # Write a program to check if a string is fully lowercase.
# # Example: Input = "hello", Output = True.
# word = "hello"
# is_lower = word.islower()  # Check if lowercase
# print("Is '{}' lowercase? {}".format(word, is_lower))
   



# #------------------------------------------------------------
# # Exercise 5: Checking if a String is Alphanumeric
# # Write a program to check if a string contains only letters 
# # and numbers.
# # Example: Input = "Python123", Output = True.
# word = "Python123"
# is_alnum = word.isalnum()  # Check if alphanumeric
# print("Is '{}' alphanumeric? {}".format(word, is_alnum))




# #------------------------------------------------------------
# # Exercise 6: Checking if a String is Alphabetic
# # Write a program to check if a string contains only letters.
# # Example: Input = "Python", Output = True.
# word = "Python"
# is_alpha = word.isalpha()  # Check if alphabetic
# print("Is '{}' alphabetic? {}".format(word, is_alpha))




# #------------------------------------------------------------
# # Exercise 7: Checking if a String is Numeric
# # Write a program to check if a string contains only numbers.
# # Example: Input = "12345", Output = True.
# word = "12345"
# is_digit = word.isdigit()  # Check if numeric
# print("Is '{}' numeric? {}".format(word, is_digit))




# #------------------------------------------------------------
# # Exercise 8: Removing Extra Spaces
# # Write a program to remove leading and trailing spaces.
# # Example: Input = "  hello  ", Output = "hello".
# word = "  hello  "
# stripped_word = word.strip()  # Remove spaces
# print("Stripped string: '{}'".format(stripped_word))




# #------------------------------------------------------------
# # Exercise 9: Length Validation
# # Write a program to validate that a string has at least 5 
# # characters. Prompt the user repeatedly until they enter a 
# # valid string.
# while True:
#     user_input = input("Enter a string with at least 5 characters: ")
#     if len(user_input) >= 5:
#         break  # Exit loop if valid
#     print("String too short. Try again.")
# print("Valid string: {}".format(user_input))




#------------------------------------------------------------
###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 10: Validating Uppercase Input
# Scenario: You are entering product codes into a system, and 
# all codes must be in uppercase letters (e.g., "ABC123").

# while True:
#     code = input("enter a code ")
#     if code.isupper():
#         print("it is correct")
#         break
#     else:
#         print("code have to be in uppercase ")

   









#------------------------------------------------------------
# Exercise 11: Validating Alphanumeric Input
# Scenario: A username field only accepts alphanumeric characters
# (letters and numbers) without special symbols.
# .isalnum()
# while True:
#     username = input("enter a username ")
#     if username.isalnum():
#         print("it is correct ")
#         break
#     else:
#         print ("username needs to be in alphanumeric ")




#------------------------------------------------------------
# Exercise 12: Validating Numeric Input
# Scenario: You are collecting a phone number that must contain 
# only numeric characters.


# while True:
#     number = input("enter a 8 digit phone number ")
#     if number.isdigit():
#         print("valid number ")
#         break
#     else:
#         print("number needs to be in numbers ")





#------------------------------------------------------------
# Exercise 13: Checking for Substrings
# Scenario: You are searching for the word "Python" in user 
# feedback to categorize responses related to Python programming.
# word = "python"
# sentence = "the python is a snake"

# if word in sentence:
#     print(f"{word} is in [{sentence}] ")
# else:
#     print(f"{word} is not in [{sentence}] ")




#------------------------------------------------------------
# Exercise 14: Replacing Parts of a String
# Scenario: A user entered their old email address, and you 
# need to replace it with a new domain (e.g., from "@old.com" to "@new.com").






#------------------------------------------------------------


# Assignment 3: Counting Uppercase Letters
# Scenario: Count the number of uppercase letters in a paragraph.

# Example:
# Input: "The Quick Brown Fox Jumps Over The Lazy Dog."
# Output: "Number of uppercase letters: 9"

# Input: "this is a simple paragraph with no uppercase letters."
# Output: "Number of uppercase letters: 0"

# Input: "Hello, World! Python Is Amazing."
# Output: "Number of uppercase letters: 5"

# s = "The Quick Brown Fox Jumps Over The Lazy Dog"
# uppers = 0
# for i in s:
#     if i.isupper():
#         uppers = uppers + 1
#         print(uppers)

####################################################
# Assignment 1: Password Validation
# Scenario: Validate a password to ensure it is at least 8 characters long and contains:
# # - At least one uppercase letter.
# # - At least one lowercase letter.
# # - At least one digit.

# # Example:
# # Input: "Secure123"
# # Output: "Valid password"

# # Input: "password"
# # Output: "Invalid password: missing uppercase letter and digit"

# # Input: "PASSWORD123"
# # Output: "Invalid password: missing lowercase letter"

# password = input("type in a password ")
# upperok = False 
# lowerok = False
# digitok = False

# for c in password:
#     if c.isupper() == True:
#         upperok = True

#     if c.islower() == True:
#         lowerok = True

#     if c.isdigit() == True:
#         digitok = True


# if upperok == True and lowerok == True and digitok == True and len(password)>= 8:
#     print(f"password is valid")
# else:
#     print(f"password is invalid")




# num1 = 5
# num2 = 10

# if num1 > num2:
#     print("num1 is bigger")
# elif num1 < num2: 
#     print("num1 is not bigger")
# else:
#     print("They are equal")

#############################################
# Assignment 16: Sentence Validation
# Scenario: Ensure a sentence starts with a capital letter and ends with a period.

# Example:
# Input: "The quick brown fox jumps over the lazy dog."
# Output: "Valid sentence"

# Input: "the quick brown fox jumps over the lazy dog"
# Output: "Invalid sentence: does not start with a capital letter and does not end with a period"

# Input: "Hello world"
# Output: "Invalid sentence: does not end with a period"

# sentence = "The quick brown fox jumps over the lazy dog."

# check that the first character is a number, and the last character is lowercase

sentence = input("enter a sentence ")
first = sentence[0] 
last = sentence[-1]
if first.isdigit() == True and last.islower():
    print("sentence is valid ")

else:
    print("sentence is invalid ")


# if first.isupper() == True:
#     firstok = True

# else:
#     print("false")






# if last == ".":
#     print("true")

# else:
#     print("false")
    

