import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))

total_cost = sum(cost)
dp = [[0] * (total_cost + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(total_cost + 1):
        dp[i][j] = dp[i-1][j]
        if j >= cost[i-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-cost[i-1]] + mem[i-1])

for j in range(total_cost + 1):
    if dp[n][j] >= m:
        print(j)
        break