import sys,heapq
input = sys.stdin.readline

n = int(input())
l = [[] for _ in range(n)]
cs = []
rooms = []
res = [0]*(n+1)
rc = 0

for _ in range(n):
    a,b,c = map(int, input().split())
    heapq.heappush(cs,(b,c,a))
for _ in range(n):
    b,c,a = heapq.heappop(cs)
    if rooms and rooms[0][0] <= b:
        end,idx = heapq.heappop(rooms)
    else:
        rc += 1
        idx = rc
    res[a] = idx
    heapq.heappush(rooms,(c,idx))

print(max(res))
for i in res[1:]:
    print(i)