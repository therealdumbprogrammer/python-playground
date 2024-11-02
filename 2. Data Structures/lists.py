# Write a Python program that:

# Creates a list of 5 numbers entered by the user.
# Displays the list.
# Sorts the list in ascending order and displays it.
# Converts the list to a tuple and displays the tuple.
# Asks the user for a number to check if it's in the tuple and displays an appropriate message.

input_list = []

for i in range(1, 6):
    input_list.append(int(input(f"Enter number {i}")))

print(f"Original list: {input_list}")

print(f"Sorted list: {sorted(input_list)}")

input_tuple = tuple(input_list)
print(f"Converted to tuple: {input_tuple}")

while True:
    to_search = int(input("Enter a number to search: "))
    if to_search in input_tuple:
        print("Number found")
    else:
        print("Number not found")

    should_exit = input("Enter 'q' to quit or 'c' to continue")
    
    if should_exit == 'q':
        break



