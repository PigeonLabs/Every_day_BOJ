import sys
input = sys.stdin.readline
from collections import deque

m,n = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

move = [(-1,0),(1,0),(0,-1),(0,1)]

q = deque([(0,0)])
visited = [[-1]*m for _ in range(n)]
visited[0][0] = 0

while True:
    y,x = q.popleft()
    if y == n-1 and x == m-1:
        print(visited[y][x])
        break
    for dy,dx in move:
        ny,nx = y+dy, x+dx
        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx]==-1:
            if arr[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny,nx))
            else:
                visited[ny][nx] = visited[y][x]
                q.appendleft((ny,nx))