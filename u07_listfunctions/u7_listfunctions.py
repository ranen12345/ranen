# # ###################################################
# # # Part 1: Learning Exercises

# # # Exercise 1: Accessing List Elements by Index
# # # Write a program to access and print the first, second, and last 
# # # elements of a list using indexing.

# # # fruits = ["apple", "banana", "watermelon"]
# # fruits = ["apple" , "banana" , "watermelon"]

# # print(fruits[2])




# # #------------------------------------------------------------
# # # Exercise 2: Adding Elements to a List
# # # Write a program to add an element to the end of a list using 
# # # append(), and add another element at a specific index using 
# # # insert().





# # #------------------------------------------------------------
# # # Exercise 3: Using del() to Remove an Element by Index
# # # Write a program to delete an element at a specific index.
# # # Example: Remove the second color.
# # print(fruits)
# # del(fruits[1])
# # print(fruits)




# # #------------------------------------------------------------
# # # Exercise 4: Using remove() to Remove an Element by Value
# # # Write a program to remove a specific element by its value.
# # # Example: Remove "green" from the list.
# # # colors = ["red", "green", "blue", "yellow"]
# # # colors.remove("green")  # Remove by value
# # # print("Colors after removal: {}".format(colors))
# # print(fruits)
# # fruits.remove("durain")
# # print(fruits)



# # #------------------------------------------------------------
# # # Exercise 5: Using pop() to Remove and Retrieve an Element
# # # Write a program to remove the last element of a list using pop().
# # # Example: Remove and print the last color.
# # # colors = ["red", "green", "blue", "yellow"]
# # # removed_color = colors.pop()  # Remove the last element
# # # print("Removed color: {}".format(removed_color))
# # # print("Colors after pop: {}".format(colors))

# # print(fruits)
# # lastfruit= fruits.pop()
# # print(fruits)
# # print(lastfruit)



# # #------------------------------------------------------------
# # # Exercise 6: Modifying Elements in a List
# # # Write a program to change the second element in a list to "pink."
# # # colors = ["red", "green", "blue"]
# # # colors[1] = "pink"  # Modify value at index 1
# # # print("Modified colors: {}".format(colors))

# # print(fruits)
# # fruits[1]="spikefruit"
# # print(fruits)


# # #------------------------------------------------------------
# # # Exercise 7: Membership Check
# # # Write a program to check if "blue" is in the list.
# # # colors = ["red", "green", "blue"]
# # # if "blue" in colors:
# # #     print("Blue is in the list.")
# # # else:
# # #     print("Blue is not in the list.")

# # checkfruit = input("enter a fruit name ")
# # if checkfruit in fruits:
# #     print(f"{checkfruit} is in the list)")
# # else:
# #     print(f"{checkfruit} is not in the list")

# # for i in fruits:
# #     print(i)











# ###########################################################
# # Part 2. IN-CLASS Practice Exercises

# # Exercise 9: Summing Numbers in a List
# # Write a program to calculate the sum of numbers in a list.
# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
#          756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
#          2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
#          6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
#          6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
#          4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]
# sum=0
# for i in list1:
#     sum += i
# # print(sum)






# #------------------------------------------------------------
# # Exercise 10: Finding the Maximum and Minimum
# # Write a program to find the largest and smallest numbers in 
# # a list using max() and min().
# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
#          756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
#          2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
#          6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
#          6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
#          4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

# largest = max(list1)
# smallest = min(list1)
# # print(largest)
# # print(smallest)







# #------------------------------------------------------------
# # Exercise 11: Iterating Through a List with Indices
# # Write a program to print each element in a list with its index.
# fruits = ["apple", "banana", "cherry"]

# # # 2nd way
# # for i in range(len(fruits)): #0, 1, 2  >> i here means the index
# #     print(fruits[i]) # value e.g. apple
# #     print(i) # index
    

# # for i in range(len(fruits)):
# #     print(fruits[i])
# #     print(i)

# #------------------------------------------------------------
# # Exercise 12: Reversing a List
# # Write a program to reverse the order of elements in a list.
# cities = ["New York", "London", "Paris", "Tokyo"]


# # [start:stop:step]
# cities2 = cities[::-1] # this works for string and list
# # [::-1] means from start to the end, in -1 direction (reverse)
# print(cities2)


# #------------------------------------------------------------
# # Exercise 13: Sorting a List
# # Write a program to sort a list of numbers in ascending order.
# list1 = [2944,4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]


# # sortedlist = sorted(list1,reverse=True)
# # print(sortedlist)




#------------------------------------------------------------
# Exercise 14: Removing Specific Index with del()
# Write a program to remove the third element in a list using del.
# Then print the updated list.
list1 = [2944,4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]
del(list1[2])
print(list1)





#------------------------------------------------------------
