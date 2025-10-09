import random

print("welcome to number guessing game")
print("I am thinking of a number between 1 and 100")


difficulty = input("choose the difficulty. Type 'easy' or 'hard': ").lower()

#genrate a number 
random_number = random.randint(1,100)
#print(random_number)
##########

attempts = 0
if difficulty == "easy":
    attempts+=10
elif difficulty == "hard":
    attempts+=5

print(f"You have {attempts} attempts remaining to guess the number. ")
##############
while attempts!=0:
    guessed_number = int(input("make a guess: "))
    attempts -=1
    if guessed_number==random_number:
        print("you won!")
        attempts = 0
    elif guessed_number>random_number:
        print(f"You have {attempts} attempts remaining to guess the number. ")
        print("Too High")
    elif guessed_number<random_number:
        print(f"You have {attempts} attempts remaining to guess the number. ")
        print("Too low")
###################
