MOD = 100999

t = int(input())
nums = [int(input()) for _ in range(t)]
mx = max(nums)

dp = [0] * (mx + 1)
dp[0] = 1

for i in range(1, mx + 1):
    for j in range(mx, i - 1, -1):
        dp[j] = (dp[j] + dp[j - i]) % MOD

for n in nums:
    print(dp[n])