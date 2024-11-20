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

def cycle(parent,a,b):
    if find_parent(parent, a) == find_parent(parent, b):
        return True
    return False

n,m = map(int,input().split())
parent = [0] * (1 + n)
for i in range(1, 1 + n):
  parent[i] = i

l = []
for i in range(m):
    a,b,c = map(int,input().split())
    l.append((c,a,b))
l.sort()

count = 0
res = []
for c,a,b in l:
    if cycle(parent,a,b):
        continue
    union_parent(parent,a,b)
    count += 1
    res.append(c)
    if count==n-1:
        break

print(sum(res[:-1]))