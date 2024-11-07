MAX = 1000
MOD = 1000000
DP = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(MAX+1)]
DP[1][0][0], DP[1][0][1], DP[1][1][0] = 1, 1, 1
for N in range(1, MAX):
    DP[N+1][0][0] = (DP[N][0][0] + DP[N][0][1] + DP[N][0][2])%MOD
    DP[N+1][0][1] = DP[N][0][0]
    DP[N+1][0][2] = DP[N][0][1]
    DP[N+1][1][0] = (DP[N][1][0] + DP[N][1][1] + DP[N][1][2] +
                     DP[N][0][0] + DP[N][0][1] + DP[N][0][2])%MOD
    DP[N+1][1][1] = DP[N][1][0]
    DP[N+1][1][2] = DP[N][1][1]

n = int(input())
print((DP[n][1][0] + DP[n][1][1] + DP[n][1][2] + DP[n][0][0] + DP[n][0][1] + DP[n][0][2])%MOD)