


# PART D

# 1.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def get_status(self):
        if self.score >= 70:
            return "PASS"
        
        return "FAIL"

student1 = Student("Alenka", 99)
student2 = Student("Slavoj", 95)
student3 = Student("Friedrich", 65)
student4 = Student("Ludwig", 66)
student5 = Student("David", 75)
student6 = Student("Anne", 78)

# 2.

students = []

students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)
students.append(student5)
students.append(student6)

# 3.

for student in students:
    print(student.name, student.score)

# 4-5.

for student in students:
    print(student.name, student.get_status())

# 6.

passing_students = [student for 
                    student in students 
                    if student.get_status() == "PASS"]

for student in passing_students:
    print (student.name, student.score)