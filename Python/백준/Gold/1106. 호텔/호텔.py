C, N = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(N)]
dp = [10**9] * (C + 1)
dp[0] = 0
for cost, gain in cities:
    for k in range(C + 1):
        nk = k + gain
        if nk > C:
            nk = C
        if dp[nk] > dp[k] + cost:
            dp[nk] = dp[k] + cost
print(dp[C])