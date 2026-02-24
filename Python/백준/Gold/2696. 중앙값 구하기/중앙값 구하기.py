import sys,heapq
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    l,r = [],[]
    c = 0
    arr = []
    while len(arr) < m:
        arr.extend(map(int, input().split()))
    ans = []
    for i, t in enumerate(arr):
        if len(l) == len(r):
            heapq.heappush(l, -t)
        else:
            heapq.heappush(r, t)
        if r and -l[0] > r[0]:
            left = -heapq.heappop(l)
            right = heapq.heappop(r)
            heapq.heappush(l, -right)
            heapq.heappush(r, left)
        if (i&1) == 0:
            ans.append(-l[0])
    print(len(ans))
    for i in range(0, len(ans), 10):
        print(*ans[i:i+10])