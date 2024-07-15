import sys
r, c = map(int, sys.stdin.readline().split())
graph = [ list(sys.stdin.readline().rstrip()) for _ in range(r) ]
tmp = set()
cnt = 1
dx = [ 0, 0, -1, 1 ]
dy = [ -1, 1, 0, 0 ]
def dfs(x, y, count):
    global cnt
    cnt = max(count, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] not in tmp:
                tmp.add(graph[nx][ny])
                dfs(nx, ny, count+1)
                tmp.remove(graph[nx][ny])
tmp.add(graph[0][0]) #7
dfs(0, 0, cnt)
print(cnt)