# Write a Python program that:

# Creates two sets with user-inputted numbers.
# Displays the sets.
# Finds and displays the union, intersection, and difference (set1 - set2) of the two sets.
# Creates a dictionary from the union set where each key is a number from the set and the value is the square of the key.
# Displays the dictionary.

s1 = input("Enter numbers for Set 1 (separated by spaces):")
s2 = input("Enter numbers for Set 2 (separated by spaces):")

set1 = set(s1.split())
set2 = set(s2.split())

union_set = set1 | set2
print(f"Union {union_set}")

in_set = set1 & set2
print(f"Intersection {in_set}")


