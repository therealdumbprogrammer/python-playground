# Task:
# Define a function named calculate_statistics that:

# Takes a list of numbers as a parameter.
# Calculates the sum, average, and maximum of the numbers.
# Returns all three values.
# Call the function with a sample list and unpack the returned values into separate variables.

# Print the sum, average, and maximum in a formatted way.

def calculate_statistics(numbers):

    if numbers:
        total_sum = sum(numbers)
        avg = total_sum / len(numbers)
        maximum = max(numbers)
    
    return total_sum, avg, maximum

numbers = [10, 20, 30, 40, 50]
total, average, maximum = calculate_statistics(numbers)
print(f"Sum: {total}")      # Output: Sum: 150
print(f"Average: {average}")  # Output: Average: 30.0
print(f"Maximum: {maximum}")  # Output: Maximum: 50
