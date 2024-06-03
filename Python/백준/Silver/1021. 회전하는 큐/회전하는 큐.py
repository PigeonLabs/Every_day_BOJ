from collections import deque

n,m = map(int,input().split())
q = deque(range(1,n+1))
l = list(map(int,input().split()))
c = 0
for i in l:
    a = q.index(i)
    if a<=len(q)//2:
        q.rotate(-a)
        c += a
        q.popleft()
    else:
        q.rotate(len(q)-a)
        c += len(q)-a
        q.popleft()
print(c)