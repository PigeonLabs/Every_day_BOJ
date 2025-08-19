import sys
input = sys.stdin.readline

def add(x, w, v):
    f[x] += 1
    if x in val:
        val[x].append((w, v))
    else:
        val[x] = [(w, v)]

n, m = map(int, input().split())
val = dict()
f = [0] * (n + 1)

for _ in range(n - 1):
    a, b, v = map(int, input().split())
    add(a, b, v)
    add(b, a, v)

s = f.index(1)
pref = {s: 0}
path = [s]
res = 0
prev = 0
cur = s

def dist(a, b):
    stack = [(a, -1, 0)]
    while stack:
        cur, p, acc = stack.pop()
        if cur == b:
            return acc
        for to, w in val[cur]:
            if to != p:
                stack.append((to, cur, acc + w))

for _ in range(m):
    a, b = map(int, input().split())
    print(dist(a, b))