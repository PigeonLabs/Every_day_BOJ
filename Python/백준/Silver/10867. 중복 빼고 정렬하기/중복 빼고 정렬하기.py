import sys,heapq
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)
last = 10**8
while arr:
    x = heapq.heappop(arr)
    if x != last:
        print(x)
        last = x