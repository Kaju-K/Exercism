def second(combination):
    return combination[1]

class School:
    def __init__(self):
        self.students = []
        self.grades = []
        self.expectations = []
        self.relations = []

    def add_student(self, name, grade):
        if name not in self.students:
            self.students.append(name)
            self.grades.append(grade)
            self.expectations.append(True)
        else:
            self.expectations.append(False)
        self.relations = list(zip(self.students, self.grades))
        self.relations.sort()
        self.relations.sort(key=second)

    def roster(self):
        return [student[0] for student in self.relations]

    def grade(self, grade_number):
        return [student[0] for student in self.relations if student[1] == grade_number]

    def added(self):
        return self.expectations
