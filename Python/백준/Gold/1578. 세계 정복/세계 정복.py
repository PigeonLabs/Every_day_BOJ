import sys
input = sys.stdin.readline

n,k = map(int, input().split())
l = list(map(int, input().split()))

hi = sum(l)//k
lo = 0
res = 0

while lo <= hi:
    mid = (lo + hi) // 2
    s = 0
    for x in l:
        s += min(x, mid)
        if s >= k * mid:
            break
    if s >= k * mid:
        res = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(res)