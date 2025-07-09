import sys,bisect
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n,m,k = map(int, input().split())
l = sorted(list(map(int, input().split())))
c = list(map(int, input().split()))

idx = {v : i for i,v in enumerate(l)}
p = {x: x for x in l}

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

for i in c:
    cur = find(l[bisect.bisect_right(l, i)])
    print(cur)
    if idx[cur] + 1 < len(l):
        p[cur] = find(l[idx[cur] + 1])