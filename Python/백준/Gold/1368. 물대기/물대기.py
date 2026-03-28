import sys,heapq
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = list(range(n + 1))
q = []
for i in range(1,n+1):
    heapq.heappush(q,(int(input()),0,i))
for i in range(1,n+1):
    t = list(map(int, input().split()))[i:]
    for j in range(i+1,n+1):
        heapq.heappush(q,(t[j-i-1],i,j))

x = 0
res = 0
while q:
    cost, a, b = heapq.heappop(q)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost
        x += 1
        if x == n:
            break
print(res)
