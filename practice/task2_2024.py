'''
Task 2

A school has a new computer network. The following program allows students
to create a username and password to log onto the network.
'''
list_usernames = ["StudentNo1","JaneJones","ABC123"]
# username = input("Please enter a username: ")
# password = input("Please enter a password: ")

'''
6. Edit the program so that it checks to see if the username entered exists in the list.
If it does not exist in the list, it must store the username in the list.

If it does not exist in the list, the program must loop
until a username is entered that does not already exist in the list.

Save your program. [4]
'''
# # Write and test your code here
# while True: 
#     username = input("Please enter a username: ")
#     if username in list_usernames:  
#         print("already in the list: ") 
#     else:
        
#         list_usernames.append(username) 
#         break
print(list_usernames)




'''
7. Edit your program so that it checks if the password:

- contains at least one numeric character
- contains at least one special character from: @!/?
- is at least 8 characters in length

The program should loop until the password fulfils all the three requirements.

Use suitable input and output messages

Save your program [6]
'''
# Write and test your code here
# while True: 
#     username = input("Please enter a username: ")
#     if username in list_usernames:  
#         print("already in the list: ") 
#     else:
        
#         list_usernames.append(username) 
#         break



password = input("Please enter a password: ")

# print(list_usernames)

# specials = "@!/?"



# print(gotnumber)

if len(password) >= 8:
    print("accepted")
else:
    print("not accepted")

gotnumber = False
for c in password:
    if c.isdigit():
        gotnumber= True

if gotnumber:
    print("At least 1 number. Accepted") 
else:
    print("You need at least 1 number in your password.")



