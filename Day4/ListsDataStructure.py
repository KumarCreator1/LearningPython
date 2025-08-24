States_of_India = ["Delhi","J&K","UP"]
print(States_of_India[0])  # delhi

print(States_of_India[1])
States_of_India[1] = "MP"  # replace the J&K with MP
print(States_of_India[1])  # print MP

States_of_India.append("Haryana") # update the list with Haryana at Index 3 place 4

print(States_of_India[1]) # wanted to check if J&K is still eplace by MP

print(len(States_of_India)) # for because you appended "Haryana" in list