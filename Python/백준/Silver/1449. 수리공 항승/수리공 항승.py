import sys
input = sys.stdin.readline
from collections import deque

n,t = map(int,input().split())
l = deque(sorted(map(int,input().split())))
res = 0

while True:
    s = l[0]-0.5
    while True:
        if not l:
            print(res+1)
            exit()
        elif s<l[0]<s+t:
            l.popleft()
        else:
            break
    res += 1