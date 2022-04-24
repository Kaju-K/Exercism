class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in line.split()] for line in matrix_string.split("\n")]
        self.transpose = [[self.matrix[i][j] for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]

    def row(self, index):
        return self.matrix[index-1]
    def column(self, index):
        return self.transpose[index-1]