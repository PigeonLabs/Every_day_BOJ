import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

def dfs(y, x, visited):
    if y < 0 or y >= n or x < 0 or x >= m or visited[y][x] or arr[y][x] == 0:
        return 0
    visited[y][x] = True
    size = 1
    size += dfs(y + 1, x, visited)
    size += dfs(y - 1, x, visited)
    size += dfs(y, x + 1, visited)
    size += dfs(y, x - 1, visited)
    return size

res = 0
count = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        x = dfs(i, j, visited)
        if x:
            res = max(res, x)
            count += 1
print(count)
print(res)