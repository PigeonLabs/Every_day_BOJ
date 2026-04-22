import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def conv(x):
    v = abs(x) - 1
    return v * 2 if x > 0 else v * 2 + 1

n, m = map(int, input().split())

size = 2 * n
g = [[] for _ in range(size)]
rg = [[] for _ in range(size)]

for _ in range(m):
    a, b = map(int, input().split())
    a = conv(a)
    b = conv(b)

    g[a ^ 1].append(b)
    g[b ^ 1].append(a)

    rg[b].append(a ^ 1)
    rg[a].append(b ^ 1)

visited = [False] * size
order = []

def dfs(v):
    visited[v] = True
    for nv in g[v]:
        if not visited[nv]:
            dfs(nv)
    order.append(v)

for v in range(size):
    if not visited[v]:
        dfs(v)

comp = [-1] * size

def rdfs(v, c):
    comp[v] = c
    for nv in rg[v]:
        if comp[nv] == -1:
            rdfs(nv, c)

cid = 0
for v in reversed(order):
    if comp[v] == -1:
        rdfs(v, cid)
        cid += 1

for i in range(n):
    if comp[2 * i] == comp[2 * i + 1]:
        print(0)
        break
else:
    print(1)