import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())
C = [0] + list(map(int, input().split()))
F = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    F[x].append(y)
    F[y].append(x)
visited = [0] * (N + 1)

def dfs(x):
    if visited[x]:
        return 0,0
    stack = [x]
    visited[x] = 1
    c,v = 0,0
    while stack:
        u = stack.pop()
        c += 1
        v += C[u]
        for i in F[u]:
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
    return c,v

G = []
for i in range(1, N + 1):
    c,v = dfs(i)
    if c:
        G.append((c,v))

cap = K - 1
dp = [0] * (cap + 1)

for c, v in G:
    if c > cap:
        continue
    for j in range(cap, c - 1, -1):
        dp[j] = max(dp[j], dp[j - c] + v)

print(dp[cap])