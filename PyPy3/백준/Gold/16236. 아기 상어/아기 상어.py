import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
l = []
for i in range(n):
    g = list(map(int,input().split()))
    l.append(g)
    if 9 in g:
        y = i
        x = g.index(9)
        l[y][x] = 0
    
def move(x,y,w):
    q = deque([(x,y,0)])
    cdd = []
    lc = 10**6
    while q:
        x,y,c = q.popleft()
        if not (0<=x<n and 0<=y<n) or visited[y][x] or l[y][x]>w or lc<c:
            continue
        visited[y][x] = True
        if 0<l[y][x]<w:
            lc = c
            cdd.append((y,x,c))
        m = [(0,-1),(-1,0),(1,0),(0,1)]
        for dx,dy in m:
            tx = x+dx
            ty = y+dy
            q.append((tx,ty,c+1))
    if cdd:
        cdd.sort()
        return cdd[0][1],cdd[0][0],True,cdd[0][2]
    else:
        return x,y,False,c

time,eat,weight = 0,0,2
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    fish = False
    x,y,fish,count = move(x,y,weight)
    if fish:
        time += count
        l[y][x] = 0
        eat += 1
        if eat == weight:
            eat = 0
            weight += 1
    else:
        print(time)
        exit()