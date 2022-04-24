seeds = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny",
                    "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.students = sorted(students)
        self.diagram = [[i for i in j] for j in diagram.split("\n")]
    def plants(self, name):
        cups = []
        index = self.students.index(name)
        for i in range(2):
            cups.append(seeds.get(self.diagram[i][2*index]))
            cups.append(seeds.get(self.diagram[i][2*index + 1]))
        return cups
