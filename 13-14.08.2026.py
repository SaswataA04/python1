student = {
    "R1": {"name": "Saswata", "dept": "CSE", "marks": 85},
    "R2": {"name": "RAHUL", "dept": "ECE", "marks": 72},
    "R3": {"name": "Gaurav", "dept": "CSE", "marks": 91},
    "R4": {"name": "Priyam", "dept": "IT", "marks": 78},
    "R5": {"name": "Arjun", "dept": "CSE", "marks": 88}
}

# Sort h to l
sorted_student = dict(
    sorted(student.items(), key=lambda x: x[1]["marks"], reverse=True)
)

print("Students sorted according to marks:")
for roll, details in sorted_student.items():
    print(roll, details)


# print stu with max m
max_student = max(student.items(), key=lambda x: x[1]["marks"])

print("\nStudent with maximum marks:")
print(max_student)


# avg m of stu
total = sum(details["marks"] for details in student.values())
average = total / len(student)

print("\nAverage marks:", average)

 
# stu score > avg m
print("Students scoring more than average:")
for roll, details in student.items():
    if details["marks"] > average:
        print(roll, details)