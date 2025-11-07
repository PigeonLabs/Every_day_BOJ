import sys,bisect
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
d = []

for i in range(n):
    if not d or d[-1] < l[i]:
        d.append(l[i])
    else:
        d[bisect.bisect_left(d, l[i])] = l[i]
print(len(d))