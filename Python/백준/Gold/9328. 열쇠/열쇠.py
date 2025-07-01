import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

DIR = [(-1,0),(1,0),(0,-1),(0,1)]

def addq(q, y, x, vis, maze):
    for dy, dx in DIR:
        ny, nx = y+dy, x+dx
        if 0<=ny<len(maze) and 0<=nx<len(maze[0]) \
           and not vis[ny][nx] and maze[ny][nx] != '*':
            q.append((ny,nx))
            vis[ny][nx] = True

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    maze = [list(input().rstrip()) for _ in range(h)]

    board = [['.' for _ in range(w+2)]]
    for row in maze:
        board.append(['.'] + row + ['.'])
    board.append(['.' for _ in range(w+2)])
    H, W = h+2, w+2

    line = input().strip()
    keys = set() if line == '0' else set(line)

    visited = [[False]*W for _ in range(H)]
    q = deque([(0,0)])
    visited[0][0] = True
    wait = [deque() for _ in range(26)]
    res = 0

    while q:
        y, x = q.popleft()
        cell = board[y][x]

        if cell == '$':
            res += 1
        elif 'a' <= cell <= 'z':
            idx = ord(cell) - 97
            if cell not in keys:
                keys.add(cell)
                while wait[idx]:
                    wy, wx = wait[idx].popleft()
                    q.append((wy, wx))
                    visited[wy][wx] = True
        elif 'A' <= cell <= 'Z':
            if cell.lower() not in keys:
                wait[ord(cell)-65].append((y, x))
                continue
        addq(q, y, x, visited, board)

    print(res)