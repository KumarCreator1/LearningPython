import random

ran = random.randint(0 , 10)  #return an Int X such that X = [0,10]
print(ran)

ran_flo = random.random()  # return a float between [0,1)
print(ran_flo)            

  # sometimes to extend its range we add a number                          
ran_exflo = random.random() +10 # now it generate the float in range [10.11)
print(round(ran_exflo , 3))


ran_uni = random.uniform(11  , 20) #return a float between [11,20]
print9=(ran_uni)
