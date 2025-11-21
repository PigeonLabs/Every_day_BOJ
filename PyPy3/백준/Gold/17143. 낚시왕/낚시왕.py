import sys
input = sys.stdin.readline
from collections import deque

R,C,M = map(int, input().split())
arr = [[[] for _ in range(C)] for _ in range(R)]
q = deque()
res = 0
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    arr[r-1][c-1] = [s,d,z]
    q.append([r-1,c-1,0])
for t in range(C):
    newarr = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        if arr[i][t]:
            res += arr[i][t][2]
            arr[i][t] = []
            break
    while True:
        if not q:
            break
        r,c,l = q.popleft()
        if l != t:
            q.append([r,c,l])
            break
        if not arr[r][c]:
            continue
        s,d,z = arr[r][c]
        arr[r][c] = []
        m = s
        while m:
            if d == 1:
                m %= 2*(R-1)
                nr = r - m
                if nr > 0:
                    r = nr
                    m = 0
                elif nr < 0:
                    m -= r
                    r = 0
                    d = 2
                else:
                    r = 0
                    d = 2
                    m = 0
            elif d == 2:
                m %= 2*(R-1)
                nr = r + m
                if nr < R:
                    r = nr
                    m = 0
                elif nr >= R:
                    m -= (R-1 - r)
                    r = R-1
                    d = 1
                else:
                    r = R-1
                    d = 1
                    m = 0
            elif d == 3:
                m %= 2*(C-1)
                nc = c + m
                if nc < C:
                    c = nc
                    m = 0
                elif nc >= C:
                    m -= (C-1 - c)
                    c = C-1
                    d = 4
                else:
                    c = C-1
                    d = 4
                    m = 0
            else:
                m %= 2*(C-1)
                nc = c - m
                if nc >= 0:
                    c = nc
                    m = 0
                elif nc < 0:
                    m -= c
                    c = 0
                    d = 3
                else:
                    c = 0
                    d = 3
                    m = 0
        if newarr[r][c]:
            if newarr[r][c][2] < z:
                newarr[r][c] = [s,d,z]
        else:
            newarr[r][c] = [s,d,z]
            q.append([r,c,t+1])
    arr = newarr
print(res)