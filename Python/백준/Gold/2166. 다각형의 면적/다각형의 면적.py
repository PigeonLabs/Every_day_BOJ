import sys
input = sys.stdin.readline

n = int(input())

vertices = []
for _ in range(n):
    vertices.append(tuple(map(int,input().split())))

area = 0
for i in range(n):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i + 1) % n]
    area += x1 * y2
    area -= y1 * x2

area = abs(area)/2
print(round(area,2))