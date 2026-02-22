import sys,heapq
input = sys.stdin.readline

n = int(input())
l,r = [],[]
for _ in range(n):
    t = int(input())
    if len(l) > len(r):
        heapq.heappush(r, t)
    else:
        heapq.heappush(l, -t)
    if r and l and -l[0] > r[0]:
        left = -heapq.heappop(l)
        right = heapq.heappop(r)
        heapq.heappush(l, -right)
        heapq.heappush(r, left)
    print(-l[0])