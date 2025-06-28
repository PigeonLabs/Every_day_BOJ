import sys
input = sys.stdin.readline

n = int(input())
s = set()
l = []
res = 0
ans = 0
for i in range(n):
    v,x = map(int, input().split())
    s.add(v)
    l.append((v, x))
for p in sorted(list(s)):
    q = 0
    for v,x in l:
        if p<=v:
            q += max(0, p - x)
    if res < q:
        res = q
        ans = p
if res:
    print(ans)
else:
    print(0)