import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(tuple(input().strip()))

t = 1
while True:
    res = 1
    s = set()
    for i in range(n):
        if l[i][-t:] in s:
            res = 0
            break
        else:
            s.add(l[i][-t:])
    if res:
        print(t)
        break
    t += 1
