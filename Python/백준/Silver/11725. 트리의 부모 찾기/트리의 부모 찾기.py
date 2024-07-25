import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque([1])
vertices = [[0] for _ in range(n+1)]
res = [0,1]+[None for _ in range(n-1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    vertices[a].append(b)
    vertices[b].append(a)

while q:
    t = q.popleft()
    for v in vertices[t]:
        if res[v]==None:
            res[v] = t
            q.append(v)

for i in res[2:]:
    print(i)