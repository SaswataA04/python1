#Create a class Student with attributes name, department, roll number. Initialize the attributes. With constructor
# display the record of students using show method and define the five student object and show the records of five students.



class Student:
    def __init__(self, name, department, roll_no):
        self.name = name
        self.department = department
        self.roll_no = roll_no

    def show(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Roll Number:", self.roll_no)
        print("--------------------")



s1 = Student("Saswata", "CSE", 101)
s2 = Student("Rahul", "CSE", 102)
s3 = Student("Ankit", "ECE", 103)
s4 = Student("Priya", "IT", 104)
s5 = Student("Riya", "CSE", 105)


s1.show()
s2.show()
s3.show()
s4.show()
s5.show()
