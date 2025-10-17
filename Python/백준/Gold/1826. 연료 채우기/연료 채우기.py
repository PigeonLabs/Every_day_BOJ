import sys, heapq
input = sys.stdin.readline

n = int(input())
c = 0
gasq = []
gasn = []

for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(gasq, (a, b))
end, now = map(int, input().split())

while now < end:
    while gasq and gasq[0][0] <= now:
        a, b = heapq.heappop(gasq)
        heapq.heappush(gasn, -b)
    if not gasn:
        print(-1)
        exit()
    now += -heapq.heappop(gasn)
    c += 1
print(c)