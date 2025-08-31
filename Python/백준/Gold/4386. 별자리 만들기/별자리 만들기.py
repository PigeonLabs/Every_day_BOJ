import sys, math
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

n = int(input())
star = [list(map(float, input().split())) for _ in range(n)]

edges = []
for i in range(n):
    xi, yi = star[i]
    for j in range(i+1, n):
        xj, yj = star[j]
        w = math.hypot(xi - xj, yi - yj)
        edges.append((w, i, j))

edges.sort()

parent = list(range(n))
rank = [0]*n

res = 0.0
picked = 0
for w, u, v in edges:
    if union(u, v):
        res += w
        picked += 1
        if picked == n-1:
            break

print(res)