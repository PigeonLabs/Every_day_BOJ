import sys
input = sys.stdin.readline
from collections import deque

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((a,b,c))
    graph[b].append((b,a,c))
v1,v2 = map(int,input().split())

def bfs(start,end):
    res = [10**9 for _ in range(n+1)]
    res[start] = 0
    q = deque(graph[start])
    while q:
        a,b,c = q.popleft()
        if res[a]+c < res[b]:
            res[b] = res[a]+c
            q.extend(graph[b])
    return res[end]

ans = min(bfs(1,v1)+bfs(v1,v2)+bfs(v2,n),bfs(1,v2)+bfs(v2,v1)+bfs(v1,n))
if ans>=10**9:
    print(-1)
else:
    print(ans)