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

l = []
res = 0
cc = 0
v,e = map(int,input().split())
parent = [0] * (1+v)
for i in range(1,1+v):
    parent[i] = i
for i in range(e):
    a,b,c = map(int,input().split())
    l.append((c,a,b))
l.sort()

for c,a,b in l:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        res += c
        cc += 1
        if cc==v-1:
            break

print(res)