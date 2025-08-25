import random


alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

li_password = []
password = ""
# gettin user requirements
nr_lett = int(input("how many letters you want in your password: "))
nr_symbols = int(input("how many symbols you want in your password: "))
nr_number = int(input("how many number you want in your password: "))

# store the password in list
for lett in range(1,nr_lett+1):
    li_password.append(random.choice(alph))

for lett in range(1,nr_symbols+1):
    li_password.append(random.choice(symbols))

for lett in range(1,nr_number+1):
    li_password.append(random.choice(number))

total_length = nr_lett+nr_number+nr_symbols
random.shuffle(li_password)
# concatenate the element of list to make a password
for i in range(0,total_length):
    password+= li_password[i]

print(password)