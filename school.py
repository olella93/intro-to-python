class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def course_average(self):
        count = 0
        for student in self.students:
            count += student.marks

        print(count / len(self.students))


#creating course instance
course = Course("Python")


course.add_student(Student("Titus", 20, 85))
course.add_student(Student("Bob", 22, 90))
course.add_student(Student("Charlie", 19, 78))


course.course_average()