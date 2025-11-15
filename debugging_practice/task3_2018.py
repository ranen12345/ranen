# students = False
# while students == False:       #change to false
#     comp = int(input("Enter the Computing test score "))   #add int
#     math = int(input("Enter the Mathematics test score " ))#add ""
#     joint_score = comp + math  #change to math
#     if comp >= 100 and math >= 100:   #change to >=
#         print("Student is awarded a gold award")
#     elif (comp >= 100 or math >= 100) and joint_score >= 180:      #change ands and ors
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ").upper() #check for uppercase
#     if more_scores == 'N':
#         students = False   #change to false
#     else:
#         students = True













colour_list = ['red','green', 'blue','orange', 'purple','yellow']
colour_to_find = input("Which colour would you like to search for? ")
items = len(colour_list) #change to colour_list
item_number = 0
colour_found = False
while colour_found == False: #change to false
    while item_number < items: #should be smaller than items
        if colour_list[item_number] == colour_to_find:    #double equal and :
            print("There are " + str(items) + " colours in the list, " + colour_to_find + " is item " + str(item_number + 1) + " in the list.")   # change item to items and iten to item
            colour_found = True
            item_number = item_number 
        elif item_number == items - 1:
            print("The colour is not in the list. ")
            colour_found = True  #must be true
            item_number = items
        else:
            item_number += 1 #increment












            