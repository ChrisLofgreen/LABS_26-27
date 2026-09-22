


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
student3 = Student("GW Friedrich")
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

    def update_score(self, new_score):
        if new_score > 0 and new_score <= 100:
            self.score = new_score
        else:
            raise ValueError("Scores must be between 1 and 100")

class Teacher:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, teacher, course_description="blank"):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.course_description = course_description

    def add_student(self, student):
        if student.name != "" and student.score > 0:
            self.students.append(student)
        else:
            raise ValueError(
                "Student has to have a name and a score above 0"
            )

    def students_in_course(self):
        counter = 0
        for student in self.students:
            counter += 1

        return counter

    def list_of_passed(self):
        list_of_passed = [student for student 
                          in self.students 
                          if student.pass_check() == "PASS"]

        return list_of_passed

    def score_above(self, threshold):
        for student in self.students:
            if student.score >= threshold:
                print(student.name)

        return ""


# 5-6.

teacher1 = Teacher("Anne with an 'e'")
course1 = Course("Social Skills", teacher1)

student1 = Student("Alenka", 95)
student2 = Student("Slavoj", 92)
student3 = Student("GW Friedrich", 89)
student4 = Student("Ludwig von", 32)
student5 = Student("Ludwig van", 65)
student6 = Student("Ann", 68)



course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)
course1.add_student(student4)
course1.add_student(student5)
course1.add_student(student6)

# 7-8. Added ValueError to add_student() in Course: "Student has to have a name and a score above 0"

# 9. 

student7 = Student("Axl", 95)
student8 = Student("Joe", 92)
student9 = Student("Courtney", 89)
student10 = Student("Sebastian", 32)
student11 = Student("Gary", 65)
student12 = Student("Vince", 68)

teacher2 = Teacher("Mick")
course2 = Course("Posing 101", teacher2)

course2.add_student(student7)
course2.add_student(student8)
course2.add_student(student9)
course2.add_student(student10)
course2.add_student(student11)
course2.add_student(student12)

#print(course2.name,":", course2.teacher.name)

#for student in course2.students:
#    print(student.name, student.score)

#for student in course2.list_of_passed():
#    print(student.name)

#print(course2.students_in_course())

# 10
'''
print(f"\nCOURSE SUMMERY: {course1.name.upper()}\n\nTeacher: {course1.teacher.name}\nStudents in course: {course1.students_in_course()}\n")
print("Students who passed (apologies for choice of words):")
for student in course1.list_of_passed():
    print(student.name)
'''


# PART G

# 1.

student1.update_score(80)
#print(student1.score)

# 2.

# print(course2.score_above(90))

# 3.
'''
for student in course1.students:
    print(student.name, student.score)

print("")

for student in course2.students:
    print(student.name, student.score)
'''

# 4.

course1.course_description = "This is a course for anyone who often find themselves in trouble while being around other people."
print(course1.course_description)

# I added "course_description" since it is inherantly connected to any object created by the Course class.
# If it was an indiviual object it would create extra complexity with some kind of matching.