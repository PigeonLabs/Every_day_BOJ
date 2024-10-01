import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

g = int(input())
p = int(input())

parent = [i for i in range(g + 1)]

for i in range(p):
    t = int(input())
    root = find(t)
    
    if root == 0:
        print(i)
        exit()
    
    union(root, root - 1)

print(p)