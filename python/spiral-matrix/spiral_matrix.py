from itertools import cycle

def spiral_matrix(size):
    matrix = [[None] * size for _ in range(size)]
    row, column = 0,0
    direction = cycle(((0, 1), (1, 0), (0, -1), (-1, 0)))
    dr, dc = next(direction)
    for number in range(size**2):
        matrix[row][column] = number + 1
        if (not(0 <= row + dr < size) or
            not(0 <= column + dc < size) or
            matrix[row + dr][column + dc] is not None):
            dr, dc = next(direction)
        row += dr
        column += dc
    return matrix