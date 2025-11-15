group_1 = []
group_2 = []
group_3 = []
count = 0   #put initial as zero (2)
flag = True
while flag:
    first_name = input("Please enter the child's name: ").upper()
    # first_name = first_name[1]
    first_letter = first_name[0]  #first_letter not first_name (1)  # change it to zero (5)
    age = int(input("Please enter the child's age: "))  #add int  (3)
    if first_letter <= "A" and first_letter >= "M" and age > 10:   # less than or equal to A and >= M
        group_1 = group_1 + [first_name]
    elif first_letter > "M" and age > 10:  # it is > not >=(4)   # cannot be or must be and (5)
        group_2 = group_2 + [first_name]
    elif age <= 10: #must be greater or equal to 10 (9)
        group_3 = group_3 + [first_name]
    count += 1 # remove indent (7)
    more = input("Do you have another child to enter, Y or N?: ")
    if more == "N":  #change from Y to N so that code can stop (6)
        flag = False

print("You have entered the names of", count, "children")  # change to count (8)
print("The members of group 1 are", group_1)
print("The members of group 2 are", group_2)
print("The members of group 3 are", group_3)


























































