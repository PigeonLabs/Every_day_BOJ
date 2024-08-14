import sys
input = sys.stdin.readline
from collections import deque

n =int(input())
l = [[] for _ in range(n+1)]
idx,ans = 1,0

for _ in range(n-1):
    d = list(map(int,input().split()))
    l[d[0]].append((d[1],d[2]))
    l[d[1]].append((d[0],d[2]))
for i in range(2):
    res = [10**6 for _ in range(n+1)]
    q = deque([idx])
    res[idx] = 0
    while q:
        p = q.popleft()
        for dst,time in l[p]:
            if res[p]+time < res[dst]:
                res[dst] = res[p]+time
                q.append(dst)
    idx = res.index(max(res[1:]))
    ans = max(ans,res[idx])

print(ans)