# # # fobj = open("filename.txt", "a")


# # # fobj.write("\nnext year will be best")

# # # fobj.close()




# # with open("filename.txt", "r") as fobj:
# #     content = fobj.read()
# #     print(content)





 


# # fobj = open("filename.txt", "r")
# # content = fobj.read()
# # print(content)



# # counta = 0
# # for i in content:
# #     if i == "a":
# #         counta = counta + 1
# # print(f"There are {counta} A in the file")
       


# # with open("filename.txt" , "r") as fobj:
# #     daylist = fobj.readlines()

# #     for day in daylist:
# #         print(day)



# # planetslist = ["mercury\n", "jupyter\n", "earth\n", "saturn\n", "venus\n"]
# # with open("planets.txt" , "w") as fobj:
# #     fobj.writelines(planetslist)
# tasklist = [] 
# while True:
#     task = input("what do you have to do today? ")
#     tasklist.append(task + "\n")
#     proceed = input("Type N to stop ").upper()
#     if proceed == "N":
#         with open("task.txt" , "a") as fobj:
#             fobj.writelines(tasklist)



#         break


# # A text file shapes.txt stores a list of shapes with a comma between each value.  

# # The current contents of shapes.txt are: 
# # star,sphere,square,triangle 

# # A text file colours.txt stores a list of colours with a comma between each value.  

# # The current contents of colours.txt are: 
# # red,yellow,green,blue 

# # A program reads the data from each file and creates a dictionary of the values 
# # so that each shape has an associated colour. 
# # The first value in each file will be joined, for example, star and red. 

# # The data is stored in a global dictionary with the identifier data_stored. 


# date_store = []

# read the colours.txt
# read the shapes.txt



sentence = "Today is saturday"
with open("newfile.txt", "w") as fileobj:
    fileobj.write(sentence)
