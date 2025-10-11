def totalcash():
    penny =int(input("no. of penny:"))*0.01
    dime =int(input("no. of dime:"))*0.05
    nickel =int(input("no. of nickel:"))*0.10
    quarter =int(input("no. of quarter:"))*0.25
    return penny+dime+nickel+quarter

cash = totalcash()
print(cash)