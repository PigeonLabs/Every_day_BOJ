import sys,heapq
input = sys.stdin.readline

n, m = map(int, input().split())

H = [[int(c) for c in input().strip()] for _ in range(n)]

hq = []
visited = [[False]*m for _ in range(n)]

for y in range(n):
    for x in range(m):
        if y in (0, n-1) or x in (0, m-1):        # 가장자리
            heapq.heappush(hq, (H[y][x], y, x))
            visited[y][x] = True

water = 0
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while hq:
    h, y, x = heapq.heappop(hq)
    for dy, dx in dirs:
        ny, nx = y+dy, x+dx
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            visited[ny][nx] = True
            nh = H[ny][nx]
            if nh < h:
                water += h - nh
            heapq.heappush(hq, (max(h, nh), ny, nx))

print(water)