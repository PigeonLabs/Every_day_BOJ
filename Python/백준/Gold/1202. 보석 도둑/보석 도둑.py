import sys,heapq
input = sys.stdin.readline

n,k = map(int, input().split())
jw = []
hq = []
c = []
for i in range(n):
    m,v = map(int, input().split())
    heapq.heappush(jw, (m, v))
for i in range(k):
    heapq.heappush(c, int(input()))

res = 0
for _ in range(k):
    w = heapq.heappop(c)
    while len(jw) and jw[0][0] <= w:
        m,v = heapq.heappop(jw)
        heapq.heappush(hq, (-v, m))
    if hq:
        res += -heapq.heappop(hq)[0]
print(res)