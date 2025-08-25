import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(input()) for _ in range(5*n+1)]
res = [0,0,0,0,0]
for i in range(n):
    for j in range(m):
        s = 0
        for k in range(4):
            if arr[i*5+1+k][j*5+1] == '*':
                s += 1
        res[s] += 1
print(*res)