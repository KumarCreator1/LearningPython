import random

friends = ["Alice","Bob","David","virat","Rohit"]
ran_flo = random.randint(0,4)

print("The bill will be payed by:")

if ran_flo>=1 and ran_flo<3 :
    print(friends[0])
elif ran_flo>=3 and ran_flo<5 :
    print(friends[1])
elif ran_flo>=5 and ran_flo<7 :
    print(friends[2])
elif ran_flo>=7 and ran_flo<9 :
    print(friends[3])
else:
    print(friends[4])

#another way 
rand_int = random.randint(0,4)
print(f"the bill will be payed by {friends[rand_int]}")

# Anotherr way of doing it using random.choice(list) 
print(f"The bill will be payed by:{random.choice(friends)}")