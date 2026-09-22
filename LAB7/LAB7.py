


# PART D
'''
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
'''

# PART E
'''
# 1.
class Teacher:
    def __init__(self, name):
        self.name = name
# 2.
class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, name):
        self.name = name


# 3.
teacher1 = Teacher("Anne with an 'e'")
course1 = Course("Social Skills", teacher1)

# 4.
print(course1.name, ":",course1.teacher.name)

# 5.
student1 = Student("Alenka")
student2 = Student("Slavoj")
student3 = Student("GF Wilhelm")
student4 = Student("Ludwig von")
student5 = Student("Ludwig van")
student6 = Student("Ann")
# 6.
course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)
course1.add_student(student4)
course1.add_student(student5)
course1.add_student(student6)
# 7.
for student in course1.students:
    print(student.name)
'''

# PART F

# 1-4.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def pass_check(self):
        if self.score >= 70:
            return "PASS"

        return "FAIL"

class Teacher:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def students_in_course(self):
        counter = 0
        for student in self.students:
            counter += 1
        return counter

    def list_of_passed(self):
        list_of_passed = [student for student in self.students if student.pass_check() == "PASS"]
        return list_of_passed


# 5-6.

teacher1 = Teacher("Anne with an 'e'")
course1 = Course("Social Skills", teacher1)

student1 = Student("Alenka", 95)
student2 = Student("Slavoj", 92)
student3 = Student("GF Wilhelm", 89)
student4 = Student("Ludwig von", 32)
student5 = Student("Ludwig van", 65)
student6 = Student("Ann", 68)


course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)
course1.add_student(student4)
course1.add_student(student5)
course1.add_student(student6)

print(course1.students_in_course())

# 7.
for student in course1.list_of_passed():
    print(student.name)

