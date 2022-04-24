
class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.column = column
        self.position = [self.row, self.column]
        
    def can_attack(self, another_queen):
        if self.position == another_queen.position:
            raise ValueError("Invalid queen position: both queens in the same square")
        return (self.position[0] == another_queen.position[0]) or (self.position[1] == another_queen.position[1]) or (abs(self.position[0] - another_queen.position[0]) == abs(self.position[1] - another_queen.position[1]))
