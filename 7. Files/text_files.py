
print("Writing to a file")
with open("7. Files\greetings.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")

print("\nread the entire file in read mode")
with open("7. Files\greetings.txt") as file:
    print(file.read())

print("\nreading line by line")
with open("7. Files\greetings.txt") as file:
    for line in file:
        print(line.strip())

print("\nAppending data")
with open("7. Files\greetings.txt", "a") as file:
    file.write("Line 3")

print("\nReading entire file again")
with open("7. Files\greetings.txt") as file:
    print(file.read())