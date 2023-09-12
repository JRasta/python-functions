# Object Orientated Programming in Python

class Student:
    # initialise a student
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 -100

    # get a student's grade
    def get_grade(self):
        return self.grade


class Course:
    # initialise a course
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    # add a student to the course
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    # get average grade of all students on the course
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            return value / len(self.students)


# create the students
s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 17, 75)
s3 = Student('Jill', 18, 35)

# create the course
course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)

print(course.get_average_grade())
