import sys
input=sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
rep = -1
l = [[0]*(m+2)]
for _ in range(n):
    l.append([0]+list(map(int,input().split()))+[0])
l.append([0]*(m+2))



def out():
    queue = deque([(1,1)])
    visited[1][1] = 1
    while queue:
        y,x = queue.popleft()
        l[y][x] = rep
        if 0<y<n+1 and 0<x<m+1:
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (l[y+dy][x+dx]==rep+1 or l[y+dy][x+dx]==0) and visited[y+dy][x+dx]==0:
                    queue.append((y+dy,x+dx))
                    visited[y+dy][x+dx] = 1
                elif l[y+dy][x+dx]==1:
                    del_set.add((y+dy,x+dx))
                    visited[y+dy][x+dx] += 1

c_list = [True]
while True:
    visited=[[0 for _ in range(m+2)] for _ in range(n+2)]
    del_set = set()
    del_list = []
    out()
    for i,j in del_set:
        if visited[i][j]>=2:
            del_list.append((i,j))
    if len(del_list)==0:
        print(-rep-1)
        exit()
    for i,j in del_list:
        l[i][j]=rep
    rep -= 1