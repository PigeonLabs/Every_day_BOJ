import sys,heapq
input = sys.stdin.readline

n = int(input())
h = []
for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(h, (-b, a))

x = -h[0][0]
for i in range(n):
    b,a = heapq.heappop(h)
    b = -b
    x = min(x - a, b - a)
print(x)