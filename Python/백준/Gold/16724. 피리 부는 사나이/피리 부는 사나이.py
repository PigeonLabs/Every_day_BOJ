import sys
input = sys.stdin.readline

ss = 0
def dfs(y,x,res):
    dir = dict([("U", (y-1, x)), ("D", (y+1, x)), ("R", (y, x+1)), ("L", (y, x-1))])
    dy, dx = dir[grid[y][x]]
    if l[dy][dx]==0:
        l[dy][dx] = res
        dfs(dy,dx,res)
    elif l[dy][dx]==res:
        return
    else:
        global ss
        ss += 1

grid = []
n,m = map(int,input().split())
for i in range(n):
    grid.append(list(input().strip()))

l = [[0 for j in range(m)] for i in range(n)]

res = 1
for i in range(n):
    for j in range(m):
        if l[i][j] != 0:
            continue
        l[i][j] = res
        dfs(i,j,res)
        res += 1

print(res-ss-1)