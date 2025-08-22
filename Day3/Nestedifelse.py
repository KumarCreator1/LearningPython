print("welcome to rollercoaster ride")
h = int(input("enter your height: "))

if h>120:  #if first if is true then it directly execute the else
    age = int(input("enter your age: "))
    if age>18 :
        print("$12")
    else:
        print("$7")
else:
    print("you can't ride")