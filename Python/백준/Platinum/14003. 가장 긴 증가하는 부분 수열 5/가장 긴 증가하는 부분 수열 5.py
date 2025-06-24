import sys, bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

tails = []
res   = []
parent = [-1]*n

for i, x in enumerate(a):
    k = bisect.bisect_left(tails, x)
    if k == len(tails):
        tails.append(x)
        res.append(i)
    else:
        tails[k] = x
        res[k] = i

    if k:
        parent[i] = res[k-1]

L = len(tails)
lis = [0]*L
idx = res[-1]
for p in range(L-1, -1, -1):
    lis[p] = a[idx]
    idx = parent[idx]

print(L)
print(*lis)