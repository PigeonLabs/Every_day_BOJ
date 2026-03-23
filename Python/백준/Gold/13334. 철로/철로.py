import sys,heapq
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    a,b = map(int, input().split())
    if a > b:
        a, b = b, a
    heapq.heappush(q, (b, a))
d = int(input())

res = []
mx = 0
while q:
    b, a = heapq.heappop(q)
    heapq.heappush(res, a)
    while res and res[0] < b - d:
        heapq.heappop(res)
    mx = max(mx, len(res))
print(mx)