import sys,heapq
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
l = list(map(int,input().split()))

heap = []
for i in range(2*m-2):
    heapq.heappush(heap,(-l[i],i))

for i in range(m-1,n-m+1):
    heapq.heappush(heap, (-l[i+m-1], i+m-1))
    while heap[0][1] <= i - m:
        heapq.heappop(heap)
    if m-1 <= i:
        print(-heap[0][0],end=" ")