import random
graphic = [
    r"""
     +---+
         |
         |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """, "."
]



print(r"""
 _    _          _   _  _____ __  __          _   _ 
| |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
| |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
|  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
| |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
|_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|

                H A N G M A N
""")
#########################################################################




word_list = ["python", "guitar", "planet", "tiger", "castle"]

hide_word = random.choice(word_list)

# print(hide_word)
gameover = False
correct_li= []

NumberOfBlanks = len(hide_word)
blank_list = []
blank_str =""
for i in range(0,NumberOfBlanks):
    blank_list.append("_")
    blank_str+= "_"
print(blank_str)



NumberOfLives = 6
while gameover != True:
    display = ""
    print(f"you have {NumberOfLives}/6")
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

    if guess not in hide_word:
        NumberOfLives-=1
        print("you guessed wrong,You lost a live")
        print(f"you have {NumberOfLives}/6")
        if NumberOfLives == 0:
            print("You lost")
            gameover = True


    if "_" not in display:
        gameover = True
        print("You win")
    
    print(graphic[6-NumberOfLives])
