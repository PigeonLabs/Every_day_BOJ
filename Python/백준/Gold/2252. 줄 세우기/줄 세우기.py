import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
e = [0]*(n+1)
g = [[]for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    e[b] += 1

res = []
q = deque()
for i in range(1,n+1):
    if e[i]==0:
        q.append(i)

while q:
    p = q.popleft()
    res.append(p)
    for i in g[p]:
        e[i] -= 1
        if e[i]==0:
            q.append(i)

print(*res)