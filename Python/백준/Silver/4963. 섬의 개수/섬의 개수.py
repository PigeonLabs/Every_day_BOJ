import sys
input = sys.stdin.readline

def dfs(w, h, grid):
    directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    visited = [[False]*w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    for dx, dy in directions:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w:
                            if grid[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                count += 1
    return count

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(h)]  # ✅ 수정된 부분
    print(dfs(w, h, grid))