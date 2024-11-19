import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
parent = [0] * (1+n)
for i in range(1,1+n):
    parent[i] = i
for i in range(m):
    t,a,b = map(int,input().split())
    if t:
        if find_parent(parent,a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")
    else:
        union_parent(parent,a,b)