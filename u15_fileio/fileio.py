# A text file shapes.txt stores a list of shapes 
# with a comma between each value.  

# The current contents of shapes.txt are: 
# star,sphere,square,triangle 

# A text file colours.txt stores a list of 
# colours with a comma between each value.  

# The current contents of colours.txt are: 
# red,yellow,green,blue 

# A program reads the data from each file and 
# creates a dictionary of the values so that each shape
#  has an associated colour. 
# The first value in each file will be joined, for example, star and red. 

# The data is stored in a global dictionary with the identifier data_store

#########################################
# Task A 6 - marks
# The function read_values() reads the data from both files 
# and stores the data in the global dictionary data_stored.  

# The data from the shapes.txt file is used as the key 
# and the data from the colours.txt file is used as the value. 

# The function needs to work for files of any length. 
# The files will always have the same number of data values. 

# Write program code for the function read_values(). 
#########################################
# Write code for Task A here

data_stored = {} #["star", "red", "sphere", "yellow", "square", "green"]

def read_values():
    with open("shapes.txt" , "r") as shapefile:
        shapestring = shapefile.read()
        with open("colours.txt" , "r") as colourfile:
            colourstring =  colourfile.read()
          
        shapelist = shapestring.split(",")
        colourlist = colourstring.split(",")


    for i in range(len(shapelist)):
        currentshape = shapelist[i]
        currrentcolour = colourlist[i]
        data_stored[currentshape] = currrentcolour
read_values()
print(data_stored)






#########################################
# Task B -  4 marks
# The function output_result() asks the user to enter a shape 
# until the shape entered is found in the dictionary. 
# The colour for that shape is printed out. 

# Write program code for the function output_result(). 
#########################################
# Write code for Task B here



def output_result():
    while True:
        shape = input("enter a shape ").lower()
        if shape in data_stored:
            colour = data_stored(shape)
            print(f"the colour for{shape} is {colour}.")
            break
        else:
            print(f"{shape} does not exist. Try again")
output_result()
