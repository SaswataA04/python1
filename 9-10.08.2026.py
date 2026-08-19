#create list of 20 studdnt marks and perform the following opns on list 
# 1. find avg marks from list 
# 2. find out hthe no of sudents score more than avg in list 
# 3. find the marks  that max studnts scored in list 



marks = [75, 82, 67, 90, 55, 82, 76, 88, 90, 67,
         72, 81, 95, 60, 82, 78, 90, 69, 82, 85]

average = sum(marks) / len(marks)
print("Average Marks =", average)

count = 0
for mark in marks:
    if mark > average:
        count += 1

print("Number of students scoring more than average =", count)

# 3.(Mode)
frequency = {}

for mark in marks:
    if mark in frequency:
        frequency[mark] += 1
    else:
        frequency[mark] = 1

max_freq = max(frequency.values())

print("Marks scored by the maximum number of students:")
for mark, freq in frequency.items():
    if freq == max_freq:
        print(mark, "scored by", freq, "students")