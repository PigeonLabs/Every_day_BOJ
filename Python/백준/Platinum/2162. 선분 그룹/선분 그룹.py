import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    t = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if t > 0:
        return 1
    if t < 0:
        return -1
    return 0

def intersect(a, b):
    x1, y1, x2, y2 = a
    x3, y3, x4, y4 = b

    if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2):
        return False
    if max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2):
        return False

    ab1 = ccw(x1, y1, x2, y2, x3, y3)
    ab2 = ccw(x1, y1, x2, y2, x4, y4)
    cd1 = ccw(x3, y3, x4, y4, x1, y1)
    cd2 = ccw(x3, y3, x4, y4, x2, y2)

    if ab1 * ab2 == 0 and cd1 * cd2 == 0:
        return True
    return ab1 * ab2 <= 0 and cd1 * cd2 <= 0

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if e[a] < e[b]:
        a, b = b, a
    parent[b] = a
    e[a] += e[b]

n = int(input())
segments = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) > (x2, y2):
        x1, y1, x2, y2 = x2, y2, x1, y1
    segments.append((x1, y1, x2, y2))

parent = list(range(n))
e = [1] * n

for i in range(n):
    for j in range(i + 1, n):
        if intersect(segments[i], segments[j]):
            union(i, j)

groups = 0
max_size = 0
for i in range(n):
    if parent[i] == i:
        groups += 1
        if e[i] > max_size:
            max_size = e[i]

print(groups)
print(max_size)
