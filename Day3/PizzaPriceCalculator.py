print("Welcome to Pizza Hut!")
size = input("what size pizza do you want? S,M or L: ")
pep = input("do you want pepperoni Y or N? ")
ch = input("do you want cheese Y or N? ")
bill = 0

if size == "S":
    bill += 15
    if pep == "Y":
        bill += 2
    if ch == "Y":
        bill += 1

elif size == "M":
    bill += 20
    if pep == "Y":
        bill += 3
    if ch == "Y":
        bill += 1

else:
     bill += 25
     if pep == "Y":
        bill += 3
     if ch == "Y":
        bill += 1

print(f"your bill for pizza is ${bill}")