with open("FiveLetterWords.txt" , "r") as fobj:

    contents = fobj.read().split(",")
    print(contents)



fourletterwords = []


fourletterwords = [] # need empty list to store 
vowels = ["a", "e", "i", "o", "u"]


# loop through all the words in the list

# count the number of unique vowels by doing the below
    # loop through all possible vowels a, e, i, o, u
        # check if this current vowel e.g. a is in the word
            # vowelcount += 1

# if the number of vowels is 4 
    # add to fourletterwords list

for word in contents:
    vowelcount = 0
    for v in vowels:
        if v in word:
            vowelcount += 1

    if vowelcount == 4:
        fourletterwords.append(word)
print(fourletterwords)



