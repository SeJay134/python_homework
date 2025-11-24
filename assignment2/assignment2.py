# Utilities
import csv

def open_csv(csvName):
    tmp = {}
    tmp2 = []

    try:
        with open('../csv/'+csvName, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if "fields" not in tmp:
                    tmp["fields"] = row
                else:
                    tmp2.append(row)

        tmp["rows"] = tmp2
        return tmp

    except Exception as e:
        print("Error:", e)
        return None

# Task 2

read_employees = lambda: open_csv("employees.csv")

employees = read_employees()
print(employees)

# Task 3
def column_index(name_column):
    x = employees['fields'].index(name_column)
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
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

print(employee_find_2(1))

# Task 7
def sort_by_last_name():
    employees["rows"].sort(key=lambda row : row[column_index("last_name")])
    return employees["rows"]

# Task 8
def employee_dict(employee_row):
    tmp = {}
    for i in employees['fields']:
        if(i != "employee_id"):
            tmp[i] = employee_row[employees['fields'].index(i)]
    return tmp

print(employee_dict(employees["rows"][0]))

# Task 9
def all_employees_dict():
    tmp = {}
    for i in employees['rows']:
        tmp[i[0]] = employee_dict(i)
    return tmp

print(all_employees_dict())

# Task 10
import os
os.environ['THISVALUE'] = 'ABC'

get_this_value = lambda: os.getenv("THISVALUE")

print(get_this_value())

# Task 11
import custom_module

set_that_secret = lambda secret: custom_module.set_secret(secret)

set_that_secret("secret")
print(custom_module.secret)

# Task 12

def read_minutes():
    tmp1 = open_csv("minutes1.csv")
    tmp = []
    for i in tmp1["rows"]:
        tmp.append(tuple(i))
    tmp1["rows"] = tmp
    
    tmp2 = open_csv("minutes2.csv")
    tmp = []
    for i in tmp2["rows"]:
        tmp.append(tuple(i))
    tmp2["rows"] = tmp

    return tmp1, tmp2

global minutes1, minutes2
minutes1, minutes2 = read_minutes()

# Task 13

create_minutes_set = lambda: set(minutes1["rows"]).union(set(minutes2["rows"]))

global minutes_set
minutes_set = create_minutes_set()
print(minutes_set)

# Task 14
from datetime import datetime

create_minutes_list = lambda: list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), list(minutes_set)))

global minutes_list
minutes_list = create_minutes_list()
print(minutes_list)

# Task 15

def write_sorted_list():
    minutes_list.sort(key=lambda row : row[1])
    tmp = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(minutes1["fields"])
        writer.writerows(tmp)
    return tmp

write_sorted_list()