# Task:
# Define a Function modify_list:

# This function should take two arguments:
# A list of numbers.
# A function that defines how to modify each number in the list.
# The function should apply the passed-in function to each element of the list and return a new list with the modified values.
# Define Two Functions to Pass as Arguments:

# square(x): Returns the square of x.
# cube(x): Returns the cube of x.
# Use modify_list with Both square and cube Functions:

# Pass a sample list of numbers to modify_list along with square to get a list of squared numbers.
# Pass the same list to modify_list along with cube to get a list of cubed numbers.
# Print the Results:

# Display the original list, the squared list, and the cubed list in a clear format.

def modify_list(numbers, func):
    if numbers:
        return list(map(func, numbers))
    return []

original_list = [1, 2, 3, 4, 5]
squared_list = modify_list(original_list, lambda x: x**2)
cubed_list = modify_list(original_list, lambda x: x**3)

print(f"Original List: {original_list}")
print(f"Squared List: {squared_list}")
print(f"Cubed List: {cubed_list}")