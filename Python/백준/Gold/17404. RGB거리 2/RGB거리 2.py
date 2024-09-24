import sys
input = sys.stdin.readline

n = int(input())
l = []
ans = 10**8

for _ in range(n):
    l.append(list(map(int, input().split())))
for t in range(3):
    res = [[10**8,10**8,10**8] for _ in range(n)]
    res[0][t] = l[0][t]
    for i in range(1, n):
        res[i][0] = min(res[i-1][1],res[i-1][2])+l[i][0]
        res[i][1] = min(res[i-1][0],res[i-1][2])+l[i][1]
        res[i][2] = min(res[i-1][0],res[i-1][1])+l[i][2]
    for j in range(3):
        if t!=j:
            ans = min(ans,res[-1][j])
print(ans)