# Task:
# Define Functions for Arithmetic Operations:

# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)
# Implement Exception Handling:

# Handle division by zero.
# Handle invalid inputs (non-numeric values).
# Main Functionality:

# Prompt the user to enter two numbers.
# Prompt the user to select an operation.
# Perform the operation and display the result.
# Handle all possible exceptions with appropriate messages.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except:
        raise ZeroDivisionError("Can't divide by 0")
    

num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")

print("\nSelect an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

input_choice = input("Enter your choice (1-4): ")

try:
    n1 = int(num1)
    n2 = int(num2)
    choice = int(input_choice)

    if choice == 1:
        print(f"{n1} + {n2} = {add(n1, n2)}")
    elif choice == 2:
        print(f"{n1} - {n2} = {subtract(n1, n2)}")
    elif choice == 3:
        print(f"{n1} * {n2} = {multiply(n1, n2)}")
    elif choice == 4:
        print(f"{n1} / {n2} = {divide(n1, n2)}")
    else:
        print("Unsupported operation selected!")
except ValueError as ve:
    print(f"Invalid number entered {ve}")    
except ZeroDivisionError as zde:
    print(f"{zde}")