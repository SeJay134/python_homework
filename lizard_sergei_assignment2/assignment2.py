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