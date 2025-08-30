# # # # Exercise 1: Simple List Slicing
# # # # Write a program to extract the first 3 elements from a list.
# # # numbers = [10, 20, 30, 40, 50]
# # # print(numbers[:3])


# # # Exercise 2: Negative Indexing
# # # Write a program to extract the last 2 elements from a list 
# # # # # using negative indexing.
# # # # numbers = [10, 20, 30, 40, 50]
# # # # print(numbers[-2:])


# # # #------------------------------------------------------------
# # # # Exercise 4: Reversing a List Using Slicing
# # # # Write a program to reverse a list using slicing.
# # # numbers = [10, 20, 30, 40, 50]
# # # print(numbers[::-1])

# # # # word = "SINGAPORE"

# # # # print(word[::-1]) 


# # # # for i in range(1, 15, 1):
# # # #     print(i)





# # ###########################################################
# # # Part 2. IN-CLASS Practice Exercises

# # # Exercise 7: Extracting Middle Elements from a List
# # # Scenario: Extract the middle 3 elements from a list with an odd 
# # # number of elements.
# # numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

# # mid = len(numbers) // 2
# # print(numbers[mid-1])
# # print(numbers [mid])
# # print(numbers [mid+1])




# # #------------------------------------------------------------

# # # Exercise 8: Checking Palindrome in a String
# # # # Scenario: Determine if a string is a palindrome (reads the same 
# # # # backward as forward).
# # word = input("Enter a word: ")


# # reverse = word[::-1]
# # print(reverse)

# # if word == word[::-1]:
# #     print(f"{word} is a palindrome")
# # else:
# #     print(f"{word} is not a palindrome")





# #------------------------------------------------------------

# # Exercise 9: Reversing Words in a Sentence
# # Scenario: Reverse the words in a sentence manually.
# sentence = "Python is fun to learn"
# # print(sentence[::-1])

# words = sentence.split(" ") # splits each word in the sentence into a list. using space as delimiter
# print(words)
# print(words [::-1])







#------------------------------------------------------------
# Exercise 10: Validating a Substring
# Scenario: Check if a string contains only alphabets .isalpha()
text = "Hello"

if text.isalpha():
    print(f"{text} contains only alphabets")
else:
    print(f"{text} does not only contains alphabet")


# for i in text:
#     if text.isalpha():
#         print(True)
    





#---------------------------------





