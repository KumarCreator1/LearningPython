logo= '''          _________
                /        /|
               /________/ |
              |         | |
              |         | |
              |_________|/
                  ||
                  ||
                  ||
     =========================
     ||                      ||
     ||       AUCTION        ||
     ||______________________||
'''


def winner():
    winner_bid = 0
    winner_name = ""
    for key in name_bid:
        if name_bid[key]>winner_bid:
            winner_bid=name_bid[key]
            winner_name = key
    print(f"winner is {winner_name} with a bid amount of ${winner_bid}")

name_bid ={}
should_continue = True

print(logo)
while should_continue == True:
    name = input("whats your name ? : ")
    bid = int(input("What's your bid?: $"))
    name_bid[name] = bid
    print("Bid ACCEPTED.....")
    ask = input("Is there any other bidder. yes or no?; ").lower()
    if ask == "yes":
        print("\n"*50)
        print(logo)
    elif ask == "no":
        should_continue = False
        winner()