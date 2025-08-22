print("Welcome to the tip calculator")
bill = float(input("what was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
total = bill + (bill*tip)/100
ppl = int(input(" How many people to split the bill? "))
Each_pay =round(total/ppl , 2)
print(f"Each person should pay: {Each_pay}")
