# Task 3

import csv
import pprint

def read_employees():
    list_store = []
    
    try:
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                list_store.append(row)
        return list_store
            
    except Exception as e:
        print("Error:", e)
        return None

employees = read_employees()
pprint.pprint(employees)
print() # split

employees_first_last = []
for row in employees[1:]:
    x = f"{row[1]} {row[2]}"
    employees_first_last.append(x)
print(employees_first_last)

print() # split

employees_first_e = []
for name in employees_first_last:
    if "e" in name.lower():
        employees_first_e.append(name)
print(employees_first_e)