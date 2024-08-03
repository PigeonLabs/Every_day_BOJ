import sys
input = sys.stdin.readline
from collections import deque

n =int(input())
l = [[] for _ in range(n+1)]
r,maxr,ans = 0,0,0

for _ in range(1,n+1):
    d = list(map(int,input().split()))
    for k in range(1,len(d)-1,2):
        dst = d[k]
        time = d[k+1]
        l[d[0]].append((dst,time))
    if r<len(d):
        r = len(d)
        maxr = d[0]
idx = maxr
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