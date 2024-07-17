import sys
input = sys.stdin.readline
from collections import deque

r,c,t = map(int,input().split())
l = deque()
p = []
cc = 0
for i in range(r):
    lst = deque(map(int,input().split()))
    if cc == 0:
        try:
            f = lst.index(-1)
            p.append(i)
            p.append(f)
            lst[f] = 0
            cc += 1
        except:
            pass
    l.append(lst)

for _ in range(t):
    l2 = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            cnt = 0
            if l[i][j]>=5:
                diff = l[i][j]//5
                for dy,dx in ([1,0],[-1,0],[0,1],[0,-1]):
                    if 0<=i+dy<r and 0<=j+dx<c and not (p[0]<=i+dy<=p[0]+1 and p[1]==j+dx):
                        l2[i+dy][j+dx] += diff
                        cnt += 1
                l[i][j] -= diff*cnt

    for i in range(r):
        for j in range(c):
            l[i][j] += l2[i][j]

    y = p[0]
    x = p[1]
    l[y][x] = 0
    for i in range(y,0,-1):
        l[i][0],l[i-1][0] = l[i-1][0],l[i][0]
    l[y][x] = 0
    l[0].rotate(-1)
    for i in range(y):
        l[i][-1],l[i+1][-1] = l[i+1][-1],l[i][-1]
    l[y].rotate(1)
    l[y][x] = 0

    y = p[0]+1
    l[y][x] = 0
    for i in range(y,r-1):
        l[i][0],l[i+1][0] = l[i+1][0],l[i][0]
    l[y][x] = 0
    l[-1].rotate(-1)
    for i in range(r-1,y,-1):
        l[i][-1],l[i-1][-1] = l[i-1][-1],l[i][-1]
    l[y].rotate(1)
    l[y][x] = 0

res = 0
for i in l:
    res += sum(i)

print(res)