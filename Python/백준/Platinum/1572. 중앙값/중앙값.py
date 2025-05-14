import sys,bisect
input = sys.stdin.readline

n,k = map(int, input().split())
l = []
res = 0
for _ in range(n):
    l.append(int(input()))
v = l[:k]
v.sort()
res += v[(k-1)//2]
for i in range(k,n):
    bisect.insort(v, l[i])
    v.pop(bisect.bisect_left(v, l[i-k]))
    res += v[(k-1)//2]
print(res)