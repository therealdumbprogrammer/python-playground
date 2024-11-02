# Problem:
# Create a simple calculator program that:

# Asks the user to input two numbers.
# Asks the user to select an operation (+, -, *, /).
# Performs the selected arithmetic operation on the two numbers.
# Prints the result in a clear and formatted way.

n1 = int(input("Enter first number:"));
n2 = int(input("Enter second number:"));

op = input("Select an operation (+, -, *, /):");

if op == "+":
    print("Result is: " + str(n1 + n2))
elif op == "-":
    print("Result is: " + str(n1 - n2))
elif op == "*":
    print("Result is: " + str(n1 * n2))
elif op == "/":
    print("Result is: " + str(n1 / n2))
else:
    print("Unsupported operation!");            

