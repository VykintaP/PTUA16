# Create a function that sorts a list of employee records
# based on their salaries. Each employee record is a dictionary
# with name, age, and salary keys. Employees with the highest
# salaries should be printed first.


def sort_employees_by_salary(employees):
    return sorted(employees, key=lambda emp: emp['salary'], reverse=- True)

    for emp in employees:
        print(emp['salary'])


employees = [
    {'name': 'Alice', 'age': 30, 'salary': 70000},
    {'name': 'Bob', 'age': 25, 'salary': 50000},
    {'name': 'Charlie', 'age': 35, 'salary': 60000}
]
sorted_employees = sort_employees_by_salary(employees)
for emp in sorted_employees:
    print(f"Name: {emp['name']}, Age: {emp['age']}, Salary: ${emp['salary']}")

    # Expected output:

    # Name: Alice, Age: 30, Salary: $70000
    # Name: Charlie, Age: 35, Salary: $60000
    # Name: Bob, Age: 25, Salary: $50000
