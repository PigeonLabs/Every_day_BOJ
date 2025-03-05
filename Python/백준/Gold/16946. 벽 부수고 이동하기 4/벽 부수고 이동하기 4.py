import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r, c, grid, visited, comp, comp_wall):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return
    if visited[r][c] or grid[r][c] != 0:
        return
    visited[r][c] = True
    comp.append((r, c))
    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
            continue
        if grid[nr][nc] == 0:
            dfs(nr, nc, grid, visited, comp, comp_wall)
        elif grid[nr][nc] == 1:
            if (nr, nc) not in comp_wall:
                comp_wall.add((nr, nc))

def group_zeros_and_walls(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    groups = []
    groups_wall = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 and not visited[i][j]:
                comp = []
                comp_wall = set()
                dfs(i, j, grid, visited, comp, comp_wall)
                groups.append(comp)
                groups_wall.append(list(comp_wall))
    return groups, groups_wall

n, m = map(int, input().split())
grid = [list(map(int, list(input().strip()))) for _ in range(n)]

groups, groups_wall = group_zeros_and_walls(grid)
res = [row[:] for row in grid]
for i in range(len(groups)):
    for y, x in groups_wall[i]:
        res[y][x] += len(groups[i])
for i in range(n):
    print("".join(map(lambda x: str(x % 10), res[i])))