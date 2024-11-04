import csv

students = [
    ['Name', 'Age', 'Grade'],
    ['Alice', '23', 'A'],
    ['Bob', '22', 'B'],
    ['Charlie', '24', 'C']
]

with open("7. Files\csv_data.txt", "w", newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(students)

with open("7. Files\csv_data.txt") as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        print(f"{line[0]}, {line[1]}, {line[2]}")