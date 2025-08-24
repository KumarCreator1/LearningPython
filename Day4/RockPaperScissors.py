import random
import time
choice = ["Rock","Paper","Scissor"]

# choice of computer
comp_choice = random.randint(0,2)



# choice of player
my_choice = int(input("What do you choose ? type 0 for Rock 1 for Paper 2 for scissor: "))
print(f"you chose: {choice[my_choice]}")

# define condition for declaring result.
if my_choice == 0 and comp_choice == 1 :
    print(f"Computer choosed: {choice[comp_choice]}")
    time.sleep(1)
    print("You Lost")
elif my_choice == 0 and comp_choice == 2:
    print(f"Computer choosed: {choice[comp_choice]}")
    time.sleep(1)
    print("You win")
elif my_choice == 1 and comp_choice == 0 :
    print(f"Computer choosed: {choice[comp_choice]}")
    time.sleep(1)
    print("you win")
elif my_choice == 1 and comp_choice == 2 :
    print(f"Computer choosed: {choice[comp_choice]}")
    time.sleep(1)
    print("you Lost")
elif my_choice == 2 and comp_choice == 0 :
    print(f"Computer choosed: {choice[comp_choice]}")
    time.sleep(1)
    print("you Lost")
elif my_choice == 2 and comp_choice == 1 :
    print(f"Computer choosed: {choice[comp_choice]}")
    time.sleep(1)
    print("you win")
elif my_choice == comp_choice:
    print(f"Computer also choosed: {choice[comp_choice]}")
    time.sleep(1)
    print("Draw")
else:
    print("invalid input. Try Again")



