#dict

#Create a dictionary named employee, where employee ID is the key. 
#The value against employee ID is a nested dictionary that includes employee name, designation, department, and salary. 
#The dictionary consists of records of five employees.
#Perform the following operations in the dictionary. 
#Print the record of employee with employee ID E1. 
#Print the department of employee E4. 
#Print the record of employee having the maximum salary. 
#Insert a new employee record in the existing dictionary.


employee = {
    "E1": {
        "name": "Rahul",
        "designation": "Manager",
        "department": "HR",
        "salary": 60000
    },
    "E2": {
        "name": "Priya",
        "designation": "Developer",
        "department": "IT",
        "salary": 75000
    },
    "E3": {
        "name": "Amit",
        "designation": "Analyst",
        "department": "Finance",
        "salary": 55000
    },
    "E4": {
        "name": "Sneha",
        "designation": "Designer",
        "department": "Design",
        "salary": 65000
    },
    "E5": {
        "name": "Rohan",
        "designation": "Developer",
        "department": "IT",
        "salary": 80000
    }
}

# 1
print("Record of E1:")
print(employee["E1"])

# 2
print("\nDepartment of E4:")
print(employee["E4"]["department"])

# 3
max_employee = max(employee, key=lambda x: employee[x]["salary"])

print("\nEmployee with maximum salary:")
print(employee[max_employee])

# 4
employee["E6"] = {
    "name": "Ananya",
    "designation": "Tester",
    "department": "IT",
    "salary": 70000
}

print("\nDictionary after inserting E6:")
print(employee)