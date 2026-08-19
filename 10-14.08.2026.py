#create a tuple of 20 employes name . perfomr the opns- 
# 1.print each name and no of freq in list 
# 2. remove the duplicate items from tuple and find the distinct name in tuple 
# 3.print the name of emploeyye having max freq 
# 4. sort the tuple in alpha order and dispaly 
# 5. ip a specific employee name and find whethe that name  exixst in tuple or not 

employees = (
    "Rahul", "Priya", "Amit", "Rahul", "Sneha",
    "Amit", "Rohan", "Priya", "Neha", "Rahul",
    "Vikash", "Sneha", "Amit", "Rohan", "Priya",
    "Karan", "Neha", "Rahul", "Vikash", "Amit"
)

# 1
print("1. Employee Name and Frequency:")

for name in set(employees):
    print(name, ":", employees.count(name))


# 2
distinct_names = tuple(set(employees))

print("\n2. Distinct Employee Names:")
print(distinct_names)


# 3
max_frequency = max(employees.count(name) for name in set(employees))

print("3. Employee(s) having maximum frequency:")

for name in set(employees):
    if employees.count(name) == max_frequency:
        print(name, ":", max_frequency)


# 4
sorted_employees = tuple(sorted(employees))

print("\n4. Employees in Alphabetical Order:")
print(sorted_employees)


# 5
search_name = input("5. Enter employee name to search: ")

if search_name in employees:
    print(search_name, "exists in the tuple.")
else:
    print(search_name, "does not exist in the tuple.")