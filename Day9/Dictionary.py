programing_dictionary = {
    "Bug":"An error in program",
    "Function": "A pies of code that you can call and call over again",
    "Loop": "The action that ocurr again and agian",
    123:"234",
    234:456,
}

empty = {}
print(programing_dictionary["Bug"]) 
print(programing_dictionary[123]) #234

#it will add Key in the dictionary
programing_dictionary["key"]="Metal piece helps to unlock a lock"

print(programing_dictionary)

#wipe out a distionary
programing_dictionary={}  # erase all data in dictionary
print(programing_dictionary) #print {}

#change an exiting key value , let's change the value of Bug
programing_dictionary["Bug"] = "A moth in your computer"
print(programing_dictionary)