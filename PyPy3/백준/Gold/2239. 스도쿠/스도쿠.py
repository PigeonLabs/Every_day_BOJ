import sys

class Board:
    board = []
    rows = []
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty_cells = []
    _presence = [False] * 10

    def __init__(self):
        for i in range(9):
            line = list(map(int, list(sys.stdin.readline().rstrip())))
            for j in range(9):
                if line[j] == 0:
                    self.empty_cells.append((i, j))
            self.rows.append(set(line) - {0})
            self.board.append(line)
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    continue
                self.cols[j].add(self.board[i][j])
                self.boxes[i//3*3 + j//3].add(self.board[i][j])

    def place(self, row, col, value):
        self.board[row][col] = value
        self.rows[row].add(value)
        self.cols[col].add(value)
        self.boxes[row//3*3 + col//3].add(value)

    def unplace(self, row, col, value):
        self.board[row][col] = 0
        self.rows[row].remove(value)
        self.cols[col].remove(value)
        self.boxes[row//3*3 + col//3].remove(value)

    def print(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end='')
            print()

def solve(board, start=0):
    if start >= len(board.empty_cells):
        board.print()
        exit()

    row, col = board.empty_cells[start]
    for i in set([i for i in range(1, 10)]) - (board.rows[row] | board.cols[col] | board.boxes[row//3*3 + col//3]):
        board.place(row, col, i)
        solve(board, start+1)
        board.unplace(row, col, i)

board = Board()
solve(board)