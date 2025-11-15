group_1 = []
group_2 = []
group_3 = []
flag = True
while flag:
    first_name = input("Please enter the child's name: ").upper()
    first_letter = first_name[0] # 1. should be first_letter. #2 should be index 0 not 1
    age = input("Please enter the child's age: ")
    if first_letter >= "A" and first_letter <= "M" and age > 10:
        group_1 = group_1 + [first_name]
    elif first_letter >= "M" or age > 10:
        group_2 = group_2 + [first_name]
    elif age < 10:
        group_3 = group_3 + [first_name]
        count += 1
    more = input("Do you have another child to enter, Y or N?: ")
    if more == "Y":
        flag = False

print("You have entered the names of", flag, "children")
print("The members of group 1 are", group_1)
print("The members of group 2 are", group_2)
print("The members of group 3 are", group_3)



#
 # Task 3.1

# book_authors = {
#     'Winnie the pooh': 'A. A. Milne',
#     'The tale of peter rabbit': 'Beatrix Potter',
#     'The wind in the willows': 'Kenneth Grahame',
#     'The lion, the witch and the wardrobe': 'C. S. Lewis',
#     'Charlie and the chocolate factory': 'Roald Dahl'
# }

# book = input('Please enter the title of a book: ')
# add = input("Would you like to add a book> Y or N: ")
# amend = input("Would you like to change the author of a book? Y or N: ")

# book = book[1].upper + book[1:]

##################################################################
# Task 3.2

book_authors = {
    'Winnie the pooh': 'A. A. Milne',
    'The tale of peter rabbit': 'Beatrix Potter',
    'The wind in the willows': 'Kenneth Grahame',
    'The lion, the witch and the wardrobe': 'C. S. Lewis',
    'Charlie and the chocolate factory': 'Roald Dahl'
}

book = input('Please enter the title of a book: ')
add = input("Would you like to add a book> Y or N: ")
amend = input("Would you like to change the author of a book? Y or N: ")

book = book[1].upper + book[1:]
author = input("Enter the book that you want ")
print(f"{book_authors[author]} is written by [author]")




#################################################################
# Task 3.3

book_authors = {
    'Winnie the pooh': 'A. A. Milne',
    'The tale of peter rabbit': 'Beatrix Potter',
    'The wind in the willows': 'Kenneth Grahame',
    'The lion, the witch and the wardrobe': 'C. S. Lewis',
    'Charlie and the chocolate factory': 'Roald Dahl'
}

book = input('Please enter the title of a book: ')
add = input("Would you like to add a book> Y or N: ")
amend = input("Would you like to change the author of a book? Y or N: ")

book = book[1].upper + book[1:]
author = input("Enter the book that you want ")
print(f"{book_authors[author]} is written by [author]")



if amend.upper() == "Y":
    added = ("What book do you want to add")
    added_author = ("enter the author of book to be added")
    book_authors[added] = added_authors
print(book_authors)




#################################################################
# Task 3.4

book_authors = {
    'Winnie the pooh': 'A. A. Milne',
    'The tale of peter rabbit': 'Beatrix Potter',
    'The wind in the willows': 'Kenneth Grahame',
    'The lion, the witch and the wardrobe': 'C. S. Lewis',
    'Charlie and the chocolate factory': 'Roald Dahl'
}

book = input('Please enter the title of a book: ')
add = input("Would you like to add a book> Y or N: ")
amend = input("Would you like to change the author of a book? Y or N: ")

book = book[1].upper + book[1:]
author = input("Enter the book that you want ")
print(f"{book_authors[author]} is written by [author]")



if amend.upper() == "Y":
    added = ("What book do you want to add")
    added_author = ("enter the author of book to be added")
    book_authors[added] = added_author
print(book_authors)

# check every single character
# Tom 123 Dickinson
if amend.upper() == "Y":
    book_to_amend = input("enter the book to amend ")

    # starts the validation for author
    while True:
        gotnum = False # assume there is no number
        author = input("Enter the new author: ")
        for i in author:
            if i.isdigit():
                gotnum = True
                break # don't need to check the rest
        
        # after the for , 
        if gotnum:
            print("Author name cannot contain numbers.")
        else:
            # pass already
            break # because this is valid



        # if gotnum == False:
        #     break