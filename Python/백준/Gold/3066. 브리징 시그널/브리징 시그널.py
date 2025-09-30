import sys,bisect
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    d = []
    for i in range(n):
        if not d or d[-1]<l[i]:
            d.append(l[i])
        else:
            d[bisect.bisect_left(d,l[i])] = l[i]
    print(len(d))