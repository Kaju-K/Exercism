class ConnectGame:
    def __init__(self, board):
        self.board = board.split("\n")
        for index, line in enumerate(self.board):
            self.board[index] = line.strip()
            self.board[index] = self.board[index].split()
        self.transposed_board = [[self.board[i][j] for i in range(len(self.board))] for j in range(len(self.board[0]))]
    
    def get_winner(self):   
        for index, position in enumerate(self.board[0]):
            if position == "O":
                options = self.check_surrounding(self.board, 0, index)
                if options == "win":
                    return "O"
                for indexes in options:
                    result = self.check_path(self.board, indexes[0], indexes[1])
                    if result == "win":
                        return "O"
        for index, position in enumerate(self.transposed_board[0]):
            if position == "X":
                options = self.check_surrounding(self.transposed_board, 0, index)
                if options == "win":
                    return "X"
                for indexes in options:
                    result = self.check_path(self.transposed_board, indexes[0], indexes[1])
                    if result == "win":
                        return "X"
        return ""
    
    def check_path(self, board, i, j):
        options = self.check_surrounding(board, i, j)
        if options == "win":
            return "win"
        for indexes in options:
            if self.check_surrounding(board, indexes[0], indexes[1]):
                return self.check_path(board, indexes[0], indexes[1])

    def check_surrounding(self, board, i, j):
        if board == self.board:
            player = "O"
        else:
            player = "X"
        board[i][j] = "."
        if i+1 == len(board):
            return "win"
        options = []
        if j != 0:
            if board[i][j-1] == player:
                options.append([i, j-1])
            if board[i+1][j-1] == player:
                options.append([i+1, j-1])
        if board[i+1][j] == player:
            options.append([i+1, j])
        if j+1 != len(board[0]):
            if board[i][j+1] == player:
                options.append([i, j+1])
            if i != 0:
                if board[i-1][j+1] == player:
                    options.append([i-1, j+1])
        if i != 0:
            if board[i-1][j] == player:
                options.append([i-1, j])
        return options
