import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
d = set()
res = []
for _ in range(n):
    w = list(map(str, input().split()))
    c = w[0]+" "+w[1]+" "+w[2]
    if c not in d:
        d.add(c)
        res.append(w[2])
for i in sorted(Counter(res).items()):
    print(*i)