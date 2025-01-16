n = int(input())

if n <= 1:
    print(0)
    exit()
elif n == 2:
    print(1)
    exit()

dp = [0]*(n+1)
dp[1] = 0
dp[2] = 1

for i in range(3, n+1):
    dp[i] = (i-1) * (dp[i-1] + dp[i-2]) % 1000000000

print(dp[n] % 1000000000)