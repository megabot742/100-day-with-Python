import art
print(art.logo)
#Add
def add(n1,n2):
    return n1 + n2
#Subtract
def subtract(n1,n2):
    return n1 - n2
#Multiply
def multiply(n1,n2):
    return n1 * n2
#Divide
def divide(n1,n2):
    return n1 / n2
#Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = float(input("What's is the first number?: "))
    for symbol in operations:
        print(symbol)
    check = True

    while check:
        operations_symbol = input("Pick an next operation: ")
        next_num = float(input("What's is the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, next_num)
        print(f"{num1} {operations_symbol} {next_num} = {answer}")
        go = input(f"Type 'y' to continue calculating with {answer}, 's' to star again, 'e' to exit: ").lower()
        if go == "y":
            num1 = answer
        elif go == "s":
            check = False
            calculator()
        else:
            check = False

calculator()
