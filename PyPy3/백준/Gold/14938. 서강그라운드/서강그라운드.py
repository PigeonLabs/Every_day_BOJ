import sys
input = sys.stdin.readline
from collections import deque

n,m,r = map(int,input().split())
t = [0]+list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for i in range(r):
    a,b,l = map(int,input().split())
    graph[a].append((a,b,l))
    graph[b].append((b,a,l))

def bfs(start):
    res = [10**9 for _ in range(n+1)]
    res[start] = 0
    q = deque(graph[start])
    while q:
        a,b,c = q.popleft()
        if res[a]+c < res[b]:
            res[b] = res[a]+c
            q.extend(graph[b])
    return res

ans = []
for i in range(n):
    tres = 0
    tt = bfs(i+1)
    for j in range(n):
        if tt[j+1]<=m:
            tres += t[j+1]
    ans.append(tres)
print(max(ans))
