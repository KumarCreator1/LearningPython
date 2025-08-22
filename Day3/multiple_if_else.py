print("welcome to rollercoaster ride")
h = int(input("enter your height: "))
bill = 0

# elif check condithons one after each 
# untill anyone of this found true
if h>120:  
    print("you can ride the rollercoaster")
    age = int(input("enter your age: "))
    if age<12 :
        bill = 5
    elif age<=18:
       bill = 7
    else :
       bill = 12

    #  outside the if elif ladder and will
    #  be asked to everyone eligible for ride
    photo = input("do you want a photo type y for yes or n for no: ")
    # at same indentational level
    if photo == "y":
        bill += 3
    print(f"the bill is of ${bill}")
else:
    print("you can't ride")
