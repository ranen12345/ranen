







# # # ###################################################
# # # # Part 1: Learning Exercises

# # # # Exercise 1: Absolute Value of a Difference
# # # # Find the absolute difference between two numbers.
# # # # Example: Temperatures of two cities.
# # # temp1 = 33
# # # temp2 = 59
# # # difference = temp1 - temp2
# # # print(abs(difference))







# # # #------------------------------------------------------------
# # # # Exercise 2: Convert Character to ASCII
# # # # Convert a character to its ASCII code and back again.
# # # letter = H   
# # # ordh = ord(letter)
# # # print(ordh)



# # # letterH = chr(72)
# # # # print(letterH)




# # # # #------------------------------------------------------------
# # # # # Exercise 3: Generating a Random Uppercase Letter
# # # # # Generate a random uppercase letter using ASCII values.
# # # # import random
# # # # ranupper = random.randint(65,90)
# # # # ranletter = chr(ranupper)
# # # # print(ranletter)




# # # # #------------------------------------------------------------
# # # # # Exercise 4: Generate ASCII Symbols
# # # # # Generate a random special character from ASCII values.
# # # # random_symbol = chr(random.randint(33, 47))  # Printable symbols
# # # # print("Random Symbol: {}".format(random_symbol))



# # # # generate a password with 8 random special characters
# # # import random 
# # # pw = ""
# # # for i in range(8):
# # #     ranupper = random.randint(33,47)
# # #     ranletter = chr(ranupper)
# # #     pw = pw + ranletter
# # # print(pw)


# # # #------------------------------------------------------------
# # # import random
# # # pw = ""
# # # for i in range (8):
# # #     ranupper = random.randint(65,90)
# # #     ranletter = chr(ranupper)
# # #     pw = pw + ranletter
# # # print(pw)

    



# # # ## BONUS
# # # Generate a password containing the following
# # # 3 upper case letters
# # # 3 lower case letters
# # # 3 special characters
# # # 3 numbers


# # import random
# # pw = ""
# # for i in range (3):
# #     upper = chr(random.randint(65,90))
# #     lower = chr(random.randint(97,122))
# #     special =  chr(random.randint(33,47))
# #     numbers = chr(random.randint (48,57))
# #     pw = pw + upper + lower + special + numbers
# # print(pw)

# # # # BONUS BONUS: randomize the position
# # # random.shuffle() only works on list
# # newpass = list(pw) # converting a string to a list
# # random.shuffle(newpass)

# # # convert it back to string
# # password = "".join(newpass) ## joins elements in the list back into a string
# # print(password)












# # key = 4
# # encmsg = ""
# # MESSAGE = "SINGAPORE WEATHER IS VERY HOT"
# # for letter in MESSAGE: 
# #     num = ord(letter)
# #     numplus = num + key 
# #     newchar = chr(numplus)
# #     encmsg = encmsg + newchar

# # print(encmsg)





# ###########################################################
# # Part 2. IN-CLASS Practice Exercises

# # Exercise 6: Random Username Generator
# # The format is:
# # first 3 characters of first name
# # first 3 character of last name
# # plus 3 printable characters from ASCII
# # Scenario: Generate a random 9-character username using uppercase letters and digits.


# import random
# firstname = input("Enter your first name ")
# lastname = input("Enter your last name ")
# first3 = firstname[:3]
# last3 = lastname[:3]
# upper = chr(random.randint(65,90))
# lower = chr(random.randint(97,122))
# numbers = chr(random.randint (48,57))
# print(f"{first3}{last3}{upper}{lower}{numbers}")











# letters = ABCDEFGHIJKLMNOPQRSTUVWXYZ.


input('what is your name')
