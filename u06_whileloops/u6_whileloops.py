# 34 - 7

# count = 34
# while count > 6:
#     print(count)
#     count = count - 1


# supposed to ask the user to enter an age
# age must be between 1 to 100
# age must be an integer
# if not valid, ask again
while True:
    age = input("Enter an age : ")
    if not age.isdigit():
        print("age must be a number ")
    elif int(age) < 1 or int(age) > 100:
        print("age must be from 1 to 100")
    else:
        break
    





#------------------------------------------------------------
# Exercise 9: Guessing Game
# Write a program where the user has to guess a random number (generate using ra)
# between 1 and 10. Keep prompting until they guess correctly.
# import random

# rannum = random.randint(1, 10) # 
# while True:
#     number = input("guess a number ")
#     if number != rannum:
#         print ("incorrect try again ")
#     else:
#         break




#------------------------------------------------------------
# Exercise 10: Input Validation for a Password
# Write a program that keeps asking the user to enter a password.
# If the password is correct, print "Access granted."





# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: Basic While Loop
# # Write a program to print numbers from 1 to 5 using a while loop.
# # Example: Output = 1, 2, 3, 4, 5.





# #------------------------------------------------------------
# # # Exercise 2: Counting Down with While
# # # Write a program to print numbers from 5 to 1 using a while loop.
# # # Example: Output = 5, 4, 3, 2, 1.


# # i=5
# # while i > 0:
# #     print(i)
# #     i=i-1







# # #------------------------------------------------------------
# # # Exercise 3: Summing Numbers
# # # Write a program to calculate the sum of numbers from 1 to 10.
# # # Example: Output = 55.

# # 1 + 2 + 3 +4 +5 ... +10

# # count = 1
# # sum = 0
# # while count<11:
# #     sum=sum+count
# #     count=count+1
# # print(sum)



# # #------------------------------------------------------------
# # # Exercise 4: Repeating User Input
# # # Write a program that repeatedly asks the user to input a word
# # # until the user types "stop".
# # word = ""
# # while word.lower() != "stop":  # Repeat until "stop" is typed
# #     word = input("Enter a word (type 'stop' to exit): ")
# #     print("You entered: {}".format(word))

# # while True: # infinite loop
# #     word = input("Type a word. 'stop' to stop: ")

# #     if word == "stop":
# #         print("stop detected... stopping.. ")
# #         break # break will exit the loop .i.e stop the loop
# #     else:
# #         print("Continuing....")

# # while True:
# #     word=input("type a word. 'stop' to stop: ")
# #     if word== "stop":
# #         print("stop detected.... stopping")
# #         break
# #     else:
# #         print("continuing")





# # #------------------------------------------------------------
# # # Exercise 5: Validating Input
# # # Write a program to ensure a user enters a number between 1 and 10.
# # # If the user enters an invalid number, prompt again.

# # while True:
# #     num=int(input("write a number between 1 to 10: "))
# #     if num>=1 and num<=10:
# #         print("valid")
# #         break
# #     else:
# #         print("invalid")

   
# # #------------------------------------------------------------
# # # Exercise 6: Using While True for Validation
# # # Write a program to ensure the user enters a password at least 
# # # 8 characters long. Use while True to validate the input.
# # while True:  # Infinite loop for validation
# #     password = input("Enter a password (at least 8 characters): ")
# #     if len(password) >= 8:  # Validation condition
# #         break  # Exit the loop if valid
# #     print("Password too short. Try again.")
# # print("Password accepted!")

# # len("dog") # returns how long this word is 
# # if len>=("dog"):
# #     print("valid")

# # while True:
# #     password=input("enter a password(at least 8 character): ")
# #     if len(password)>=8:
# #         print("password accepted")
# #         break
# #     print("password too short. Try again.")
    
   
# ###########################################################
# # Part 2. IN-CLASS Practice Exercises
# # Exercise 7: Multiplication Table with While Loop
# # Write a program to print the multiplication table of 7 up to 10.
# # Example: 7 x 1 = 7, ..., 7 x 10 = 70.

# i=1
# num=int(input("what number do you want?"))
# while i<= 12:
#     print (f"{num} x {i} = {num * i}")
#     i=i+1








# #------------------------------------------------------------
# # Exercise 8: Sum of Even Numbers
# # Write a program to calculate the sum of even numbers between 1 
# # and 20 using a while loop. Example: Output = 110.





# #------------------------------------------------------------
# # Exercise 9: Guessing Game
# # Write a program where the user has to guess a random number 
# # between 1 and 10. Keep prompting until they guess correctly.