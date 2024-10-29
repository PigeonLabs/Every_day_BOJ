import sys,heapq
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    heapq.heappush(l,int(input()))

res = 0
for i in range(n-1):
    t = heapq.heappop(l)+heapq.heappop(l)
    res += t
    heapq.heappush(l,t)

print(res)