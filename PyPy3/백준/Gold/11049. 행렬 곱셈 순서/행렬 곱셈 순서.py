import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))
dp = [[0]*n for _ in range(n)]

for i in range(1,n):
    for j in range(n-i):
        if i==1:
            dp[j][j+1] = l[j][0]*l[j][1]*l[j+1][1]
            continue
        dp[j][j+i] = 2**32
        for k in range(j,j+i):
            dp[j][j+i] = min(dp[j][j+i],dp[j][k]+dp[k+1][j+i]+l[j][0]*l[k][1]*l[j+i][1])
print(dp[0][n-1])