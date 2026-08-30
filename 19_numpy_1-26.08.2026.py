import numpy as np

# 2D array: 5 students × 3 subjects
marks = np.array([
    [85, 78, 92],
    [67, 88, 75],
    [95, 91, 89],
    [72, 65, 80],
    [88, 76, 94]
])

print("Marks Array:")
print(marks)

# 1. Find maximum marks
maximum = np.max(marks)
print("1. Maximum marks:", maximum)

# 2. Find minimum marks
minimum = np.min(marks)
print("2. Minimum marks:", minimum)

# 3. Find average marks
average = np.mean(marks)
print("3. Average marks:", average)

# 4. Find Student ID who scored maximum marks in first subject
student_id = np.argmax(marks[:, 0])
print("4. Student ID with maximum marks in first subject:", student_id)

# 5. Find maximum marks subject-wise
max_subjectwise = np.max(marks, axis=0)
print("5. Maximum marks subject-wise:", max_subjectwise)

# 6. Find average marks subject-wise
avg_subjectwise = np.mean(marks, axis=0)
print("6. Average marks subject-wise:", avg_subjectwise)