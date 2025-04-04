N, A, B, C, D = map(int, input().split())

dp = [[0,0,0,0,0] for _ in range(N+1)]

for t in range(N):
    if dp[t][0] == 0 and t != 0:
        continue
    if t+1<=N and dp[t+1][0]<dp[t][0]+1 and dp[t][1]+1<=A:
        dp[t+1] = dp[t][:]
        dp[t+1][0] += 1
        dp[t+1][1] += 1
    if t+5<=N and dp[t+5][0]<dp[t][0]+1 and dp[t][2]+1<=B:
        dp[t+5] = dp[t][:]
        dp[t+5][0] += 1
        dp[t+5][2] += 1
    if t+10<=N and dp[t+10][0]<dp[t][0]+1 and dp[t][3]+1<=C:
        dp[t+10] = dp[t][:]
        dp[t+10][0] += 1
        dp[t+10][3] += 1
    if t+25<=N and dp[t+25][0]<dp[t][0]+1 and dp[t][4]+1<=D:
        dp[t+25] = dp[t][:]
        dp[t+25][0] += 1
        dp[t+25][4] += 1

if dp[N][0] == 0:
    print("0 0 0 0")
else:
    print(dp[N][1], dp[N][2], dp[N][3], dp[N][4])