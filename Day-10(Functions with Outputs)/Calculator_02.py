# Calculator

# add
def add(n1, n2) :
    """This will perform Addition"""
    return n1 + n2

# Subtraction
def subtract(n1, n2) :
    """This will perform Subtraction"""
    return n1 - n2

# Multiplication
def multiply(n1, n2) :
    """This will perform Multiplication"""
    return n1 * n2

# Division
def divide(n1, n2) :
    """This will perform Division"""
    return n1 / n2

operatus = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

num1 = int(input("Enter the First Number\n:"))
num2 = int(input("Enter the Second Number\n:"))

for key in operatus :
    print(key)

operation_module = input("pick an operation from the line above\n:")
Calculation_Function = operatus[operation_module]
First_answer = Calculation_Function(num1, num2)
# for symbol in operatus :
#     if operation_module == symbol :
#         answer = operatus[symbol](num1, num2)

print(f"{num1} {operation_module} {num2} = {First_answer}")

operation_module = input("pick another operation from the line above\n:")
num3 = int(input("Enter the Another Number\n:"))
Calculation_Function = operatus[operation_module]
Second_answer = Calculation_Function(First_answer, num2)

print(f"{First_answer} {operation_module} {num3} = {Second_answer}")