import sys
input = sys.stdin.readline
from collections import deque

n,l = map(int, input().split())
a = list(map(int, input().split()))
d =deque()
for i in range(n):
    t = (i,a[i])
    while d and d[-1][1] > t[1]:
        d.pop()
    d.append(t)
    while d and d[0][0] <= i - l:
        d.popleft()
    print(d[0][1], end=' ')