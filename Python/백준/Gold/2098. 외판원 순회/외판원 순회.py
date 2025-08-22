import sys
input = sys.stdin.readline

n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]

INF = 10**8
ALL = (1 << n) - 1

# dp[cur][mask] = 0에서 시작해 mask를 방문하고 cur에 '도착'하는 최소 비용
dp = [[INF] * (1 << n) for _ in range(n)]
dp[0][1 << 0] = 0

for mask in range(1 << n):
    for cur in range(n):
        if dp[cur][mask] == INF:
            continue
        if not (mask & (1 << cur)):
            continue
        for nxt in range(n):
            if mask & (1 << nxt):
                continue
            w = pos[cur][nxt]
            if w == 0:
                continue
            nmask = mask | (1 << nxt)
            if dp[nxt][nmask] > dp[cur][mask] + w:
                dp[nxt][nmask] = dp[cur][mask] + w

# 모든 도시 방문 후, 시작점(0)으로 복귀
ans = INF
for cur in range(n):
    if dp[cur][ALL] == INF:
        continue
    back = pos[cur][0]
    if back == 0:
        continue
    ans = min(ans, dp[cur][ALL] + back)

print(ans)