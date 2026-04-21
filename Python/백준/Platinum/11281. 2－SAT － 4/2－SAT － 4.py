import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def node(x):
    v = abs(x) - 1
    return v * 2 if x > 0 else v * 2 + 1

n, m = map(int, input().split())

size = 2 * n
g = [[] for _ in range(size)]
rg = [[] for _ in range(size)]

for _ in range(m):
    a, b = map(int, input().split())
    a = node(a)
    b = node(b)

    na = a ^ 1
    nb = b ^ 1

    g[na].append(b)
    g[nb].append(a)

    rg[b].append(na)
    rg[a].append(nb)

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
    ans = [0] * n
    for i in range(n):
        ans[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print(1)
    print(*ans)