import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

LOG = n.bit_length()
parent = [[0] * (n + 1) for _ in range(LOG)]
depth = [-1] * (n + 1)

q = deque([1])
depth[1] = 0

while q:
    x = q.popleft()
    for nx in g[x]:
        if depth[nx] != -1:
            continue
        depth[nx] = depth[x] + 1
        parent[0][nx] = x
        q.append(nx)

for k in range(1, LOG):
    pk = parent[k]
    prev = parent[k - 1]
    for v in range(1, n + 1):
        pk[v] = prev[prev[v]]

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    bit = 0
    while diff:
        if diff & 1:
            a = parent[bit][a]
        diff >>= 1
        bit += 1

    if a == b:
        return a

    for k in range(LOG - 1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]

m = int(input())
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    ans.append(str(lca(a, b)))

print('\n'.join(ans))