# generate a username: 
# first 3 characters of first name
# last 3 characters of last name
# + a 3-digit random number 100 - 999
# Assume name is only 2 words, Michael Tan >>> mictan568

name = input("What is your name? ")
username = name.split(" ") # username is now a list
fname = username[0]
lname = username[1]
import random
username = f"{fname[:3]}{lname[-3:]}{random.randint(100,999)}"
print(username)




###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Extracting Middle Elements from a List
# Scenario: Extract the middle 3 elements from a list with an odd 
# number of elements.
# numbers = [10, 20, 30, 40, 50, 60, 70]



# midindex =len(numbers) // 2
# print(numbers[midindex -1 : midindex+2])







#------------------------------------------------------------

# Exercise 8: Checking Palindrome in a String
# Scenario: Determine if a string is a palindrome (reads the same 
# backward as forward).
# word = input("Enter a word: ")

# if word == word[::-1]:
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")





#------------------------------------------------------------

# Exercise 9: Reversing Words in a Sentence
# Scenario: Reverse the words in a sentence manually.
# sentence = "Python is fun to learn."

# slist = sentence.split(" ")

# print(slist[::-1])



# '''
# Question 5: Slice a list into halves.
# Divide a list into two equal halves and returns both halves.
# You may assume that the list has an even number of items
# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [1, 2, 3]  [4, 5, 6]
# '''
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# midindex = len(numbers) // 2 

# half1 = numbers[:midindex] # 4[:4]
# half2 = numbers[midindex:]
# print([half1] + [half2])




# '''
# Question 7: Remove the first and last elements of a list using slicing.
# Create a function that takes a list and returns it without 
# the first and last elements.
# Example Input: [0, 1, 2, 3, 4]
# Example Output: [1, 2, 3]
# '''





# '''
# Question 8: Create a function to reverse the order of elements in a 
# list only from the second to the last but one.
# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [1, 5, 4, 3, 2, 6]
# '''






# '''
# # Question 13: 
# # Write a function called mid3(instring)
# # Extract the middle three characters from a string
# # Check that the incoming string must be an odd length, 
# # Test case 1: example input: abcdefg, example output: cde
# # Test case 2: example input: helloworld, example output: Invalid, Even length
# '''





# Exercise 1: Extracting Initials from a Name
# Scenario: A company wants to display initials for employees on ID cards.
# Given a full name, extract the initials.

# Example:
# Input: "John Michael Smith"
# Output: "J.M.S"

# Input: "Alice Bob"
# Output: "A.B"
 

# name = input("Enter your name ").upper()
# namewords = name.split(' ')
# initials = " "
# for word in namewords:
# inititals = initials + word[0] + "."
# print(initials[:-1])