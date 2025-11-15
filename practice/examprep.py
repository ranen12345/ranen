# # #------------------------------------------------------------
# # # While Loop Validation
# # #------------------------------------------------------------

# # # Exercise 10: Length Check
# # # Keep asking user for a username until it has at least 5 characters.
# # # #check if all words in a username are alphabets
# # # .isalpha()
# # # .isdigit()
# # # .isupper()
# # # .islower()
# # # .isalnum()
# # # counter = 0 #count the words that aren't alphabets
# # # username = input("Enter a username: ")
# # # for i in username:
# # #     if i.isalpha() == False:
# # #         counter = counter + 1

# # # if counter > 0:
# # #     print("Need to be all alphabets. ")
# # # else:
# # #     print("All are alphabets")







# # # while True:
# # #     username = input("Enter a username")
# # #     if len(username) < 5:
# # #         print("username must have at least 5 letters ")
# # # #     else:
# # # #         break


# # # # ----------------------------------------------------------------

# # # # # Exercise 11: Numbers Only
# # # # # Keep asking user to enter age until input contains digits only.
# # # # counter = 0
# # # # # isdigit()
# # # # age = input("enter a age: ")
# # # # for i in age:
# # # #     if i.isupp() == False:
# # # #         counter = counter + 1
# # # # if counter > 0:
# # # #     print("It must all be in number")
# # # # else:
# # # #     print("all are alphabets")
    
    




# # # # # ----------------------------------------------------------------

# # # # # Exercise 12: Uppercase Only
# # # # # Keep asking until user enters a code in uppercase letters only.
# # # # counter = 0
# # # # # .isupper()
# # # # code = input("enter a code")
# # # # for i in code:
# # # #     if not i.isupper():
# # # #         counter = counter + 1

# # # # if counter > 0:1
# # # #     print("must be all uppercase")
# # # # else:
# # # #     print("correct code")

# # # while True:
# # #     continue = input("do you want to continue (Y/N)")
# # #     if continue.upper() == "Y":
# # #         print("continueing")
# # #     else:
# # #         break
    
# # # ----------------------------------------------------------------

# # # Exercise 13: Lowercase Only
# # # # Keep asking until user enters an email in lowercase only.





# # # # ----------------------------------------------------------------

# # # # Exercise 14: Password Validation
# # # # Keep asking until user enters a password with length >= 8.





# # # # ----------------------------------------------------------------

# # # # # Exercise 15: Date Validation
# # # # # Keep asking until user enters a date in format MM-YYYY.
# # # # # Ensure the date is between 01-1900 and 12-2025.


# # # # while True:
# # # #     date = input("enter a date :")
# # # #     date = date.split("-")
# # # #     print(date)
# # # #     if len(date[0]) == 2 and len(date[1]) == 4 and int(date[1]) > 1900 and int(date[1]) < 2025:
# # # #         print("Date is valid. ")
# # # #         break
# # # #     else:
# # # #         print("Date is invalid. ")

# # # # You have been asked to create a word game program for two players.

# # # # The program must:

# # # # ·       Allow player 1 to input a word that will be converted to lower case by the program after entry. The program must ask for another word each time the player enters a word that is more than 10 letters.

# # # # ·       Output a message to state how many letters are in the word input by player 1.

# # # # ·       Allow player 2 to enter a single lower case letter (on 10 separate occasions)

# # # # ·       Search for each letter input by player 2, in the word input by player 1

# # # # ·       Output “It is letter number X in the word.” Every a letter is found. X must be replaced by the position of the letter in the word.

# # # # ·       Output “That letter is not in the word.: when player 2 inputs a letter that is not in the word.

# # # # ·       Output “You have no entered 10 letters.” When player 2 has input all 10 letters.

# # # # ·       Output “What is the word entered by player 1?” after player 2 has input all 10 letters, and allow player 2 to enter the word. This is converted to lower case by the program.

# # # # ·       Output “That is the correct word. You win!” if player 2 inputs the same word as player 1.

# # # # ·       Output “That is not the correct word. Player 1 wins!” if player 2 does not input the same word as player 1.
# # # while True:
# # #     word = input("Player 1, enter a word: ").lower() #for player 1 to enter a code
# # #     if len(word) > 10:
# # #         print("cannot be more than 10")
# # #     else:
# # #         break

# # # print(f"Player 1's word contains {len(word)} letters")
# # # for i in range(10):
# # #     letter = input("Player 2, guess a letter. ").lower()
# # #     if letter in word:
# # #         print(f"It is letter number {word.index(letter) + 1} in the word. ")
# # #     else:
# # #         print("This letter is not in the word")
    



# # # marks = input("enter your marks: ")
# # # if marks >= "75" or marks <= "100":
# # #     print("you got an A")
# # # elif marks >= "60" or marks <= "74":
# # #     print("you got a B")
# # # elif marks >= "50" or marks <= "59" :
# # #     print("you got a C")
# # # elif marks >= "35" or marks <= "49":
# # #     print("you got a D")
# # # elif marks >= "0" or marks <= "34":
# # #     print("you got a F")
# # # elif marks < 0 or marks > 100:
# # #     print("invalid only can be from 0 to 100")



# # # for i in range(3):

# # #     pw = "sg2025!"
# # #     password = input("Enter a password ")
# # #     if password == pw:
# # #         print("Password correct!")
# # #         break
# # # else:
# # #     print("Account Locked")















# # sentence = input("Enter a sentence. ")
# # punctuation = ["!", "?", "," ]
# # new_sentence = ""
# # for i in sentence:
# #     if i not in punctuation:
# #         new_sentence += i
# # print(new_sentence)












# firstword = input("Enter the first word. ")
# secondword = input("Enter the second word. ")
# while True: 
#     anagram = False

#     for i in firstword:
#         if i in secondword:
#             anagram = True

#     for i in secondword:
#         if i in firstword:
#             anagram = True
            
#     if anagram == False:
#         break

#     if len(firstword) == len(secondword):
#         anagram = True
#     else:
#         anagram = False
#     break
# if anagram == True:
#     print("It is an anagram. ")
# else:
#     print("It is not an anagram")


sentence = "Hi,how,is,your,day"

wordlist = sentence.split(",")

print(wordlist)