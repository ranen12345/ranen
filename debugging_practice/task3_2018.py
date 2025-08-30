students = False
while students == False:       #change to false
    comp = int(input("Enter the Computing test score "))   #add int
    math = int(input("Enter the Mathematics test score " ))#add ""
    joint_score = comp + math  #change to math
    if comp >= 100 and math >= 100:   #change to >=
        print("Student is awarded a gold award")
    elif (comp >= 100 or math >= 100) and joint_score >= 180:      #change ands and ors
        print("Student is awarded a silver award")
    elif comp >= 75 and math >= 75:
        print("Student is awarded a bronze award")
    else:
        print("NO award this time, keep trying")
    more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ").upper() #check for uppercase
    if more_scores == 'N':
        students = False   #change to false
    else:
        students = True