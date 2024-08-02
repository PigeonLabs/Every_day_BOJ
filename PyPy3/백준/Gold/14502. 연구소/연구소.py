import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations as cb

n, m = map(int, input().split())
l,vi,em = [],[],[]
ans = 0

for i in range(n):
    a = list(map(int, input().split()))
    l.append(a)
    for v in range(m):
        if a[v]==2:
            vi.append(i*m+v)
        elif a[v]==0:
            em.append(i*m+v)

for c in cb(em,3):
    tl = [i[:] for i in l]
    for i in c:
        tl[i//m][i%m] = 1
    q = deque()
    for i in vi:
        q.append((i//m,i%m))
    while q:
        y,x = q.popleft()
        for dy,dx in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
            if 0<=dy<n and 0<=dx<m and tl[dy][dx]==0:
                tl[dy][dx] = 2
                q.append((dy,dx))
    ans = max(ans,sum(t.count(0) for t in tl))

print(ans)