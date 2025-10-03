def add(n1,n2):
    return n1+n2

def devide(n1,n2):
    return n1/n2

def multiply(n1,n2):
    return n1*n2

def sub(n1,n2):
    return n1-n2

operation_dictionary = {
    "+":add,
    "-":sub,
    "*":multiply,
    "/":devide
}

def calculate():
    first_number = int(input("What's the first number?: "))
    op_key = input("choose an operation + - *  / ")
    second_number = int(input("What's the second number?: "))

    result = operation_dictionary[op_key](first_number,second_number)
    return result

loop = False

while loop == False:
    ask = input("want to start a new calcuation(N) or continue with the current result(C) or stop calculator(S)")
    if ask =="S":
        print("Goodbye!")
        break
    elif ask == "N":
        result = calculate()
        print(result)
    elif ask == "C":
        op_key = input("choose an operation + - * /")
        second_number = int(input("What's the second number?: "))
        result = operation_dictionary[op_key](result,second_number)
        print(result)
