import random
import time

print("Here we go! coin is the air.....")
time.sleep(1)
print("it'coming down.....")
time.sleep(1.5)
print("and it's a")
ran_flo = random.uniform(0,10)

if ran_flo > 0 and ran_flo <= 5 :
    print("HEADS")
else:
     print("TAILS")