print('''Welcome to Treasure Island.
Your mission is to find the treasure''')

d1 = input("left or right? ").lower()

if d1 == "right" :
    print("Game over you loosed the game")
elif d1 == "left":
    d2 = input("want to swim or wait").lower()
    if d2 == "wait":
        d3 = input("which door you want to choose red yellow or blue").lower()
        if d3 == "yellow" :
            print("you won the game")
        if d3 == "red":
            print("burned by fire Game Over")
        if d3 == "blue":
            print("Eaten by Beasts. Game Over")
        else:
            print("Game Over")

    else:
        print("game over")
else:
    print("Game over")  