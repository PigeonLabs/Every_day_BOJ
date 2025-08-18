import sys,heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr,-int(input()))
for _ in range(n):
    print(-heapq.heappop(arr))