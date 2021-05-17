import random
# Introduction
print("Welcome to the Guess Game! :)")
name =input ("Enter your name: ")
print("Hello! ",name)
print ("Let's begin!!!!")

words = ["apple", "bata","close","duck","elephant","flight","geography"]

word = random .choice(words)

print("guess the word")
# chossing turns

while True:
    turns = int (input("turns >"))
    if  turns >= 10 :
        print (" go a head !")
        break
    elif  turns <= 16 and turns >10:
        print (" go a head !")
        break

    else :
        print ("out of the range !")
        continue


guesses = " "


while turns > 0:
    failed = 0

    # reading word at a time
    for char in word :
        if char in guesses:
            print (char)
        else:
            print("_")
            failed += 1
    # Win /Loose
    if failed == 0:
        print(" Congratulations!!!!  You Win!!!!!:) ", name)
        print ("The word is : ",word)
        break

# print the guess word
    guess =input('enter a word:')

    guesses += guess
    if guess  not in word:
        turns -= 1
        print('Wrong!!!!')
        print ("You have",turns ,"turns left to guess")
    else :
        print ("correct!")

    if turns ==  0:
        print ("you lose!! :<")
        print("try again##")
