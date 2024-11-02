# Write a Python program that:

# Creates a 3x3 matrix (a list of lists) with numbers entered by the user.
# Displays the matrix in a formatted way.
# Calculates the sum of each row and displays it.
# Flattens the matrix into a single list and displays it.
# Creates a new list where each element is the square of the corresponding element in the flattened list, using a list comprehension.

matrix = []

#taking input
for row in range(1, 4):
    temp = []
    for col in range(1, 4):
        temp.append(int(input(f"Enter number for row {row}, column {col}: ")))
    matrix.append(temp)

#printing
for l in matrix:
    print(l)

#row wise sum
for r in range(len(matrix)):
    sum = 0
    for c in matrix[r]:
        sum += c
    print(f"Sum of row {r+1}: {sum}")

#flatten
output = [c for r in matrix for c in r]
print(f"Flattened list: {output}")

#Squared list
squared_list = [i*i for i in output]
print(f"Squared list: {squared_list}")
