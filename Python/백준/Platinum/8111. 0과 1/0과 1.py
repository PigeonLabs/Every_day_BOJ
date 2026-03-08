import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
        continue
    d = {1: 1}
    q = deque([1])
    parent = [-1] * n
    digit = [-1] * n
    digit[1] = '1'
    while q:
        num = q.popleft()
        if num == 0:
            res = deque()
            while num != -1:
                res.appendleft(digit[num])
                num = parent[num]
            print(''.join(res))
            break
        c1,c2 = num * 10 % n, (num * 10 + 1) % n
        if c1 not in d:
            d[c1] = 1
            parent[c1] = num
            digit[c1] = '0'
            q.append(c1)
        if c2 not in d:
            d[c2] = 1
            parent[c2] = num
            digit[c2] = '1'
            q.append(c2)