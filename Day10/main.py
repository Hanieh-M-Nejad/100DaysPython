from art import logo
print("Welcome to the calculator app.")

#### operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
       "-": subtract,
       "*": multiply,
       "/": divide
       }

def answer_func(num1, num2, operation_symb):
     return operations[operation_symb](num1, num2)

def calculator():
    print(logo)
    end_calcualation = False

    num1 = float(input("Write the first number: "))
    while not end_calcualation:
        for i in operations:
            print(i)
        operation_symb = input("Pick an operation: ")
        num2 = float(input("Write the next number: "))
        answer = answer_func(num1, num2, operation_symb)
        print(f"{num1} {operation_symb} {num2} = {answer}")

        should_cont = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ").lower()
        if should_cont == 'y':
            num1 = answer
        else:
            calculator()
calculator()



