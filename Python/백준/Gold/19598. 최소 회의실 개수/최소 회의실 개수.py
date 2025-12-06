import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []
for i in range(n):
    heapq.heappush(q, list(map(int, input().split())))

res = []
heapq.heappush(res, heapq.heappop(q)[1])
for i in range(n-1):
    a,b = heapq.heappop(q)
    if res[0] <= a:
        heapq.heappop(res)
    heapq.heappush(res, b)
print(len(res))