import sys, bisect
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

d = [l[0]]

for x in l[1:]:
    if d[-1] < x:
        d.append(x)
    else:
        pos = bisect.bisect_left(d, x)
        d[pos] = x

print(len(d))