import random
word_list = ["python", "guitar", "planet", "tiger", "castle"]

hide_word = random.choice(word_list)

print(hide_word)
gameover = False
correct_li= []

NumberOfBlanks = len(hide_word)
blank_list = []
blank_str =""
for i in range(0,NumberOfBlanks):
    blank_list.append("_")
    blank_str+= "_"


while gameover != True:
    display = ""
    guess = input("Guess a letter: ").lower()
    for alph in hide_word:
        if alph == guess:
            display+= guess
            correct_li.append(guess)
        elif alph in correct_li:
            display+= alph
        else:
            display += "_"
    print(display)

    if "_" not in display:
        gameover = True
