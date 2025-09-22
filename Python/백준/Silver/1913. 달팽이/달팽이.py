import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[0] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
d = 0
num = n * n
graph[x][y] = num
num -= 1

while num:
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
        graph[nx][ny] = num
        num -= 1
        x, y = nx, ny
    else:
        d = (d + 1) % 4

for row in graph:
    print(*row)

for i in range(n):
    for j in range(n):
        if graph[i][j] == m:
            print(i + 1, j + 1)