import sys
input = sys.stdin.readline
from collections import deque

def go(stt,dst):
    q = deque([stt])
    res = [10**6 for _ in range(n+1)]
    res[stt] = 0
    while q:
        p = q.popleft()
        for d,t in l[p]:
            if res[p]+t < res[d]:
                res[d] = res[p]+t
                q.append(d)
    return res[dst]

n,m,x = map(int, input().split())
l = [[] for _ in range(n+1)]
ans = [0 for _ in range(n+1)]
for i in range(m):
    s,d,t = map(int, input().split())
    l[s].append((d,t))
for i in range(1,n+1):
    ans[i] = go(i,x)+go(x,i)

print(max(ans))