n = int(input())

dp = [0]*(n+1)
dp[0] = dp[2] = 1
for x in range(4, n+1, 2):
    res = 0
    for i in range(x//2):
        res += dp[2*i]*dp[2*(x//2-1-i)]
    dp[x] = res%987654321
print(dp[n]%987654321)