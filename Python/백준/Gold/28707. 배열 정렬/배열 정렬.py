import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
start = tuple(map(int, input().split()))
target = tuple(sorted(start))

m = int(input())
ops = []
for _ in range(m):
    l, r, c = map(int, input().split())
    ops.append((l - 1, r - 1, c))

dist = {start: 0}
hq = [(0, start)]

while hq:
    cost, cur = heappop(hq)

    if dist[cur] != cost:
        continue

    if cur == target:
        print(cost)
        break

    for l, r, c in ops:
        nxt = list(cur)
        nxt[l], nxt[r] = nxt[r], nxt[l]
        nxt = tuple(nxt)

        ncost = cost + c
        if nxt not in dist or dist[nxt] > ncost:
            dist[nxt] = ncost
            heappush(hq, (ncost, nxt))
else:
    print(-1)