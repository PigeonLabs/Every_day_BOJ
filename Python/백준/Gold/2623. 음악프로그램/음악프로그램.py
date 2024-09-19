import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    l = list(map(int,input().split()))
    for i in range(1,l[0]):
        graph[l[i]].append(l[i+1])
        indegree[l[i+1]] += 1

def topology_sort():
    res = []
    queue = deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)
    while queue:
        c = queue.popleft()
        res.append(c)
        for i in graph[c]:
            indegree[i] -= 1
            if indegree[i]==0:
                queue.append(i)
    if len(res)==n:
        for i in res:
            print(i)
    else:
        print(0)

topology_sort()