import sys
input = sys.stdin.readline

n,m = map(int,input().split())
grid = []
for i in range(n):
    l = list(map(int,input().split()))
    suml = [0]
    c = 0
    for n in l:
        c += n
        suml.append(c)
    grid.append(suml)
for i in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    res = 0
    for k in range(x1-1,x2):
        res += grid[k][y2]-grid[k][y1-1]
    print(res)