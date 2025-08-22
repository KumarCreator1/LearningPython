print("welcome to rollercoaster ride")
h = int(input("enter your height: "))

# elif check condithons one after each 
# untill anyone of this found true
if h>120:  
    age = int(input("enter your age: "))
    if age<12 :
        print("$5")
    elif age>12:
        if age<18:
            print("$7")
    elif age>18:
        print("$12")
else:
    print("you can't ride")