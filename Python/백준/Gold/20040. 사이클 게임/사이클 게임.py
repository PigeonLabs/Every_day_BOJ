import sys
input = sys.stdin.readline

n,m = map(int,input().split())
l = [i for i in range(n)]

def find(x):
    while x != l[x]:
        x = l[x]
    return x

def union(x,y):
    px = find(x)
    py = find(y)
    if px<py:
        l[py] = px
    else:
        l[px] = py


for i in range(m):
    a,b = map(int,input().split())
    if find(a) == find(b):
        print(i+1)
        exit()
    union(a,b)

print(0)