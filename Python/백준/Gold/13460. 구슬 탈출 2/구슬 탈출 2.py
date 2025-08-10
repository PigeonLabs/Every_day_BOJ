import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우
ry, rx, by, bx = 0, 0, 0, 0
arr = []

for i in range(n):
    row = list(input().strip()) 
    arr.append(row)
    for j in range(m):
        if row[j] == 'R':
            ry, rx = i, j
            arr[i][j] = '.'
        elif row[j] == 'B':
            by, bx = i, j
            arr[i][j] = '.'

def bfs():
    visited = set([(ry, rx, by, bx)])
    queue = deque([(ry, rx, by, bx, 0)])
    
    while queue:
        r_y, r_x, b_y, b_x, count = queue.popleft()

        if count >= 10:
            continue

        for dy, dx in directions:
            # move 함수로 각 구슬을 벽이나 구멍에 닿을 때까지 이동
            nr_y, nr_x, r_move_count = move(r_y, r_x, dy, dx)
            nb_y, nb_x, b_move_count = move(b_y, b_x, dy, dx)

            if arr[nb_y][nb_x] == 'O':
                continue
            if arr[nr_y][nr_x] == 'O':
                return count + 1

            if nr_y == nb_y and nr_x == nb_x:
                if r_move_count > b_move_count:
                    nr_y -= dy
                    nr_x -= dx
                else:
                    nb_y -= dy
                    nb_x -= dx
            
            if (nr_y, nr_x, nb_y, nb_x) not in visited:
                visited.add((nr_y, nr_x, nb_y, nb_x))
                queue.append((nr_y, nr_x, nb_y, nb_x, count + 1))

    return -1

def move(y, x, dy, dx):
    move_count = 0
    while arr[y + dy][x + dx] != '#' and arr[y][x] != 'O':
        y += dy
        x += dx
        move_count += 1
    return y, x, move_count

print(bfs())