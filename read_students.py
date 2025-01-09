import csv

# atidarome csv

with open('students.csv') as file:
    reader = csv.reader(file)  # skaito csv
    next(reader)  # praleisti pirma eil/antraste
    name_row, age_row, grade_row = [], [], []
    for row in reader:  # kiekvienai eilutei
        name, age, grade = row  # priskiriamos reiksmes
        name_row.append(name)
        age_row.append(int(age))
        grade_row.append(float(grade.strip()))

name_row = []
age_row = []
grade_row = []

try:
    # Open CSV file
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)  # Use csv.reader for parsing
        next(reader)  # Skip the header row (if present)

        # Process each row
        for row in reader:
            if len(row) < 3:  # Ensure row has minimum expected columns
                print(f"Skipping incomplete row: {row}")
                continue

            try:
                # Strip whitespace and parse values
                name_row.append(row[0].strip())
                age_row.append(int(row[1].strip()))
                grade_row.append(float(row[2].strip()))
            except ValueError:
                print(f"Invalid data in row: {row}")
                continue  # Skip rows with invalid data

    # Print extracted data
    for name, age, grade in zip(name_row, age_row, grade_row):
        print(f"name: {name}, age: {age}, grade: {grade}")
except FileNotFoundError:
    print("Error: The file 'students.csv' does not exist.")
