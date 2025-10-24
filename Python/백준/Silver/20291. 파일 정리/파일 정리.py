import sys
input = sys.stdin.readline

n = int(input())
d = dict()
for _ in range(n):
    s = input().strip()
    e = s[s.index(".")+1:]
    d[e] = d.get(e, 0) + 1
d = sorted(d.items())
for i,x in d:
    print(i,x)