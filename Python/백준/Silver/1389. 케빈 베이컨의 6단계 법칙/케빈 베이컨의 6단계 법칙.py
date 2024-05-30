import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        t = q.popleft()
        for i in friend[t]:
            if not visited[i]:
                visited[i] = visited[t] + 1
                q.append(i)
                
n,m = map(int,input().split())
friend = [[] for _ in range(n+1)]
res = []
for _ in range(m):
    a,b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(1,n+1):
    visited = [0]*(n+1)
    bfs(i)
    res.append(sum(visited))

print(res.index(min(res))+1)