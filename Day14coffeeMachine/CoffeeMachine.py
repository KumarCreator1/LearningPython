MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water":300,
    "milk":200,
    "coffee":100,
}

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

transaction_succ=False

#TODO 1.print report of coffee machine resources
def report():
    print(f"water: {resources["water"]}\nmilk: {resources["milk"]}\ncoffee: {resources["coffee"]} ")

#TODO 2. check resource sufficiency for order
def Resuff(ordertype):
    if ordertype=="espresso":
        if resources["water"]>=50 and resources["coffee"]>=18:
            return 1
        else:
            return 0

    elif ordertype=="latte":
        if resources["water"]>=200 and resources["coffee"]>=24 and resources["milk"]>=150:
            return 1
        else:
            return 0
        
    elif ordertype=="cappuccino":
        if resources["water"]>=250 and resources["coffee"]>=24 and resources["milk"]>=100:  
            return 1
        else:
            return 0      

#TODO 3.ask for cash #yes sir we have sufficient resources
def totalcash():
    penny =int(input("no. of penny:"))*0.01
    dime =int(input("no. of dime:"))*0.05
    nickel =int(input("no. of nickel:"))*0.10
    quarter =int(input("no. of quarter:"))*0.25
    return penny+dime+nickel+quarter

#TODO 4.upadte resources fuctionality
def upadte():
    if ordertype=="espresso":
        resources["water"]-=50
        resources["milk"]-=0
        resources["coffee"]-=18
    elif ordertype=="latte":
        resources["water"]-=200
        resources["milk"]-=150
        resources["coffee"]-=24
    elif ordertype=="cappuccino":
        resources["water"]-=250
        resources["milk"]-=100
        resources["coffee"]-=24

#TODO 5.setup the workflow
engine=True
while engine==True:
    ordertype=input("what do you want?'espresso' 'latte' 'coppuccino': ").lower()
    if ordertype == "cappuccino" or ordertype == "espresso" or ordertype == "latte":
        suffvar=Resuff(ordertype=ordertype)
        if suffvar==1:
            print("order can be fulfilled please insert cash")
            cash = totalcash()
            print(f"the cost of a {ordertype} is {MENU[ordertype]["cost"]} & tota cash inserted is {cash}")
            if cash>=MENU[ordertype]["cost"]:
                change = (cash)-MENU[ordertype]["cost"]
                round(change,2)
                print(f"here is your {ordertype} and ${change} change\n ENJOY!")
                upadte()
            else:
                print(f"sorry that cash is not enough to buy a {ordertype}")
        else:
            print("sorry sir! we don't have enough resources at the moment\n to place new order restart the machine")
            engine=False
    elif ordertype == "report":
        currentreport = report()
        print(currentreport)
    elif ordertype== "off":
        print(".......machine is turned off...... ")
        engine=False







