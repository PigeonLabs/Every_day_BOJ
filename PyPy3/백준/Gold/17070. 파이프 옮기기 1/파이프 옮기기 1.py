import sys
input = sys.stdin.readline

def dfs(y,x,s):
    global res
    if y==n-1 and x==n-1:
        res += 1
        return
    if y+1<n and x+1<n:
        if l[y+1][x+1]==0 and l[y+1][x]==0 and l[y][x+1]==0:
            dfs(y+1,x+1,2)
    if s==2 or s==3:
        if y+1<n:
            if l[y+1][x]==0:
                dfs(y+1,x,3)
    if s==1 or s==2:
        if x+1<n:
            if l[y][x+1]==0:
                dfs(y,x+1,1)

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
res = 0

dfs(0,1,1)
print(res)