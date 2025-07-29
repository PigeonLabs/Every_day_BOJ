import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 오/왼/위/아래 (0/1/2/3)
def execute(board, direction, time):
    if time == 5:
        max_tile = 0
        for row in board:
            max_tile = max(max_tile, max(row))
        return max_tile
    if direction >= 2:
        a, b, v = n - 1, -1, -1
    else:
        a, b, v = 0, n, 1

    res = []
    if direction % 2 == 0:
        for i in range(a, b, v):
            pv = 0
            line = []
            for j in range(a, b, v):
                if board[i][j] == 0:
                    continue
                if board[i][j] == pv:
                    line[-1] *= 2
                    pv = 0
                else:
                    pv = board[i][j]
                    line.append(pv)
            line += [0] * (n - len(line))
            res.append(line[::-1] if direction >= 2 else line)

    else:
        for i in range(a, b, v):
            pv = 0
            line = []
            for j in range(a, b, v):
                if board[j][i] == 0:
                    continue
                if board[j][i] == pv:
                    line[-1] *= 2
                    pv = 0
                else:
                    pv = board[j][i]
                    line.append(pv)
            line += [0] * (n - len(line))
            res.append(line[::-1] if direction >= 2 else line)
        res = [list(row) for row in zip(*res)]

    best = 0
    for d in range(4):
        best = max(best, execute(res, d, time + 1))
    return best

ans = 0
for d in range(4):
    ans = max(ans, execute(matrix, d, 0))
print(ans)
