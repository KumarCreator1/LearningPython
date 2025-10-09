
def is_prime(num):
    primehai = 1
    for each_num in range(2,num):
        if num%each_num==0 or num ==1:
            primehai = 0
            break
        
    if primehai == 0:
        print("not prime")
    elif primehai == 1:
        print("yes prime")
          
is_prime(75)