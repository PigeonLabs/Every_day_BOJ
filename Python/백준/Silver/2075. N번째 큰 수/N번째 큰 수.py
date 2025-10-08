import sys,heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    for x in map(int, input().split()):
        heapq.heappush(heap, x)
        if len(heap) > n:
            heapq.heappop(heap)
print(heap[0])