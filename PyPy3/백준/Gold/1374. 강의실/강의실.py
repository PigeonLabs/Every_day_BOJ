import heapq
import sys
input = sys.stdin.readline

n = int(input())

l = []
res = []
heapq.heappush(res,0)
for _ in range(n):
    t,s,e = map(int,input().split())
    heapq.heappush(l,(s,e))
for _ in range(n):
    s,e = heapq.heappop(l)
    m = heapq.heappop(res)
    if m<=s:
        heapq.heappush(res,e)
    else:
        heapq.heappush(res,e)
        heapq.heappush(res,m)
print(len(res))