# Task 2
import csv

def read_employees():
    dict_employees = {}
    list_store = []

    try:
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:

                if "fields" not in dict_employees:
                    dict_employees["fields"] = row
                else:
                    list_store.append(row)

        dict_employees["rows"] = list_store
        return dict_employees

    except Exception as e:
        print("Error:", e)
        return None

employees = read_employees()
print(employees)

# Task 3
def column_index(name_column):
    x = employees['fields'].index(name_column)
    print(x)
    return x

employee_id_column = column_index('employee_id')

# Task 4
first_name_column = column_index('first_name')

def first_name(row_number):
    row = employees['rows'][row_number]
    return row[first_name_column]

print(first_name(0))
print(first_name(1))

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

print(employee_find(1))
print(employee_find(5))

# Task 6
