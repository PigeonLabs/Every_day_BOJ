import sys, bisect
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
d = [l[0]]
for i in l[1:]:
    p = bisect.bisect_left(d,i)
    if p==len(d):
        d.append(i)
    else:
        d[p] = i
print(n-len(d))