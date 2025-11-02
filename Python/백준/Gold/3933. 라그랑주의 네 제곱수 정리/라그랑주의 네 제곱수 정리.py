import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

sq = [i * i for i in range(1, 200)]
dp = [0] * 40000

def dfs(length, before_sum, before_num):
    for i in range(before_num, 200):
        temp = before_sum + sq[i - 1]
        if temp >= 40000:
            break
        dp[temp] += 1
        if length <= 3:
            dfs(length + 1, temp, i)
    return

dfs(1, 0, 1)

while (n := int(input())) != 0:
    print(dp[n])