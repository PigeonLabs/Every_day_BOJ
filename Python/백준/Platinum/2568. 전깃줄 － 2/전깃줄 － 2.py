import sys,bisect
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(tuple(map(int, input().split())))
l.sort()

d = [0]
track = [0]*n
for i, (a, x) in enumerate(l):
    idx = bisect.bisect_left(d, x)
    if d[-1] < x:
        d.append(x)
    else:
        d[idx] = x
    track[i] = idx

cur = len(d) - 1
s = set()
for i in range(n-1, -1, -1):
    if track[i] == cur:
        s.add(l[i][0])
        cur -= 1
        if cur < 0:
            break

print(n-len(s))
for i, x in l:
    if i not in s:
        print(i)