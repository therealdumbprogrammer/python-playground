# Task:
# Define a Global Variable:

# Name it count and initialize it to 0.
# Create Two Functions:

# increment_local()
# Increments a local variable count by 1.
# Prints the local count.
# increment_global()
# Uses the global keyword to access the global count.
# Increments the global count by 1.
# Prints the global count.
# Call the Functions and Observe the Outputs:

# Call increment_local() twice.
# Call increment_global() three times.
# After all function calls, print the global count to verify its final value.

count = 0

def increment_local():
    count = 0
    count += 1
    print(f"Local count: {count}")

def increment_global():
    global count
    count += 1
    print(f"Global count: {count}")

increment_local()   # Output: Local count: 1
increment_local()   # Output: Local count: 1
increment_global()  # Output: Global count: 1
increment_global()  # Output: Global count: 2
increment_global()  # Output: Global count: 3
print(count)        # Output: 3

