name = "jack"
print(name)
#you can change the data in a variable 
name = "john "
print(name)

#use len() function to get string length
 # print the length of name viz. 5 
 # not 4 because there is space as well
print(len(name))

#printing the length  of input string getting from user
print(len(input("what is your name?")))

#now the input doesn't disapear/replace 
# it will be stred in a variable
username = input("what is your name?") 
length = len(username) # storing the lenth of string in length variable
print(length)
print(username) # varifies that the inputis stored in variable