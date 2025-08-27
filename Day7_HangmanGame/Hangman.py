import random

word_list = ["python", "guitar", "planet", "tiger", "castle"]

# choose a random word from list
hide_word = random.choice(word_list)
print(hide_word)


# : display blanks in place of word
NumberOfBlanks = len(hide_word)
blank_list = []
blank_str =""
for i in range(0,NumberOfBlanks):
    blank_list.append("_ ")
    blank_str+= "_ "

# print(blank_list)
print(blank_str)

# ask the user to guess a latter and maake it lowerr case
guess = input("Guess a letter: ").lower()
# NumberOfLives = NumberOfBlanks

# place the rightly gussed word in right Placeholder
display = ""
for alph in hide_word:
    if alph == guess:
        display+= guess
    else:
        display += "_ "
        # NumberOfLives-= 1
print(display)