

# # (1)
# # A private school is opening for registration. 
# # It is not known how many students will be signing up.
# # Write a program to keep track of names and students who have signed up. 

# # A "X" is entered to indicate the end of registration.
# # Print out a class list, which includes an index number and name 
# # for all students according to their registration sequence [3m]

# # Assume that the input data will always be valid.

# # Data to be tested Ivan, Dino, Ben, Ethan, Shion, Navan, X

# # # Sample Output
# # """
# # Enter a new name ('X' to quit): Ivan
# # Enter a new name ('X' to quit): Dino
# # Enter a new name ('X' to quit): Ben
# # Enter a new name ('X' to quit): Ethan
# # Enter a new name ('X' to quit): Shion
# # Enter a new name ('X' to quit): Navan
# # Enter a new name ('X' to quit): X

# # Class List
# # 1 Ivan
# # 2 Dino
# # 3 Ben
# # 4 Ethan
# # 5 Shion
# # 6 Navan
# # """
# # #####################################################################
# # students = []
# # x = 1
# # while True:
# #     name = input("enter a name('X' to quit: )")
# #     if name.upper() == 'X':
# #          break
# #     students.append(name)
# # for i in students:
# #     print(f"{x} {i}")
# #     x = x+1


# # #input()
# # #list to store
# #while loop
# #for loop





# # # (2) On the first day of school, a student informed the
# # # school that he will be joining another school nearer his home.
# # # Teacher finds that it is difficult to look for the 
# # # students' name as they were listed according to their registration sequence.

# # # Write a program to remove the name of the student. 
# # # Print out a new class list listed according to alphabetic sequence [3m]

# # # Use the following name list: ['Ivan','Dino','Ben','Ethan','Shion','Navan']

# # # Data to be tested: Dino
# # """
# # Enter name to remove: Dino

# # Class List
# # 1 Ben
# # 2 Ethan
# # 3 Ivan
# # 4 Navan
# # 5 Shion
# # """

# # # lst = sorted(lst)

# # namelist = ['Ivan','Dino','Ben','Ethan','Shion','Navan']
# # name = input("Enter name to remove: ")
# # namelist.remove(name)
# # print(namelist)

# # namelist = sorted(namelist)
# # x = 1
# # for i in namelist:
# #     print(f"{x} {i}")
# #     x = x+1




# # (3) During registration, a student's name was entered wrongly. 
# # Write a program to replace the name of a student who had registered earlier.
# # Print out a new class list [3m]

# # Assume that the input data will always be valid.

# # Data to be tested: Ben, Benedict

# """
# # Sample output
# Enter name to change: Ben
# Enter new name: Benedict

# Class List
# 1 Benedict
# 2 Dino
# 3 Ethan
# 4 Ivan
# 5 Navan
# 6 Shion
# """

# namelist = ['Ivan','Dino','Ben','Ethan','Shion','Navan']
# name = input("enter a name ")
# name2 = input("enter a name ")
# num = namelist.index(name)
# namelist[num] = name2  
# print(namelist)
# x = 1 
# for i in namelist:
#     print(f"{x} {i}")
#     x = x+1








































# Q1

# (1)
# A private school is opening for registration. 
# It is not known how many students will be signing up.
# Write a program to keep track of names and students who have signed up. 

# A "X" is entered to indicate the end of registration.
# Print out a class list, which includes an index number and name 
# for all students according to their registration sequence [3m]

# Assume that the input data will always be valid.

# Data to be tested Ivan, Dino, Ben, Ethan, Shion, Navan, X
# student_names = []

# while True:
#     name = input("Enter a new name ('X' to quit): ")
#     if name == "X":BE
#         break
#     else:
#         namelist.append[new]

# # for i in range(len(student_names)):
# #     print(f"{i + 1} {student_names[i]}")


# # (2) On the first day of school, a student informed the
# # school that he will be joining another school nearer his home.
# # Teacher finds that it is difficult to look for the 
# # students' name as they were listed according to their registration sequence.

# # Write a program to remove the name of the student. 
# # Print out a new class list listed according to alphabetic sequence [3m]

# # Use the following name list: ['Ivan','Dino','Ben','Ethan','Shion','Navan']

# # Data to be tested: Dino

# student_names = ['Ivan','Dino','Ben','Ethan','Shion','Navan']
# name_to_remove = input("Enter name to remove: ")
# if name_to_remove in student_names:
#     student_names.remove(name_to_remove)
#     print(student_names)
# else:
#     print(f"Name '{name_to_remove}' is not inside")
