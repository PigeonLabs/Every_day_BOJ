import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
l = [[] for _ in range(n+1)]
for i in range(m):
    s,d,v = map(int,input().split())
    l[s].append((s,d,v))
for i in l:
    i.sort(key=lambda x : x[2])
stt,dst = map(int,input().split())

res = [10**8 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
path = [[] for _ in range(n+1)]

q = deque()
res[stt] = 0
for s,d,v in l[stt]:
    if v<res[d]:
        res[d] = v
        path[d].append(s)
visited[stt] = True
q.append(l[stt][0][1])
while q:
    a = q.popleft()
    for s,d,v in l[a]:
        if visited[d]==False and res[s]+v<res[d]:
            res[d] = res[s]+v
            path[d] = path[s]+[s]
    visited[a] = True
    mn = 10**8
    c = 0
    for i in range(n+1):
        if res[i]<mn and visited[i]==False:
            mn = res[i]
            c = i
    if c==0:
        break
    else:
        q.append(c)
        
path[dst].append(dst)

print(res[dst])
print(len(path[dst]))
print(*path[dst])