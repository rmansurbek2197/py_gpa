class Student:
    def __init__(self, name):
        self.name = name
        self.courses = {}

    def add_grade(self, course, grade):
        self.courses[course] = grade

    def gpa(self):
        return sum(self.courses.values()) / len(self.courses)


class University:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def top_students(self):
        return sorted(self.students.values(), key=lambda s: s.gpa(), reverse=True)
