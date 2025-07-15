import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for length in range(1, n + 1):
    for s in range(n - length + 1):
        e = s + length
        k = n - (e - s) + 1
        if length == 1:
            dp[s][e] = l[s] * k
        else:
            dp[s][e] = max(dp[s + 1][e] + l[s]*k, dp[s][e - 1] + l[e - 1]*k)

print(dp[0][n])