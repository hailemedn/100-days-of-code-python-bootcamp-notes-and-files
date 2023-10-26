import os
from art import logo

os.system("cls")
# add
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    end_of_operation = False

    num1 = float(input("What is the first number? "))
    while not end_of_operation:
        # lists the keys in operation
        for operator in operation:
            print(operator)
        operator_symbol = input("pick an operation from the line above: ")
        num2 = float(input("What is the next number? "))

        if operator_symbol not in operation:
            print("invalid operator")
        else:
            calculation_function = operation[operator_symbol]
            answer = calculation_function(num1, num2)
            print(f"{num1} {operator_symbol} {num2} = {answer}")

        continue_operation = input(f"Do you want to continue operation with {answer}, type \"y\" to continue, \"n\" to start over, \"exit\" to exit: ").lower()
        if continue_operation == "y":
            num1 = answer
            os.system("cls")
        elif continue_operation == "n":
            end_of_operation = True
            os.system("cls")
            # recursive function
            calculator()
        elif continue_operation == "exit":
            end_of_operation = True
            print("Bye")
        else:
            end_of_operation = True
            print("Invalid Input")
      
    
calculator()