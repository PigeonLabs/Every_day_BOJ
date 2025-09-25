import sys
input = sys.stdin.readline

n,c = map(int, input().split())
d = dict()
nums = list(map(int, input().split()))
for i in range(n):
    x = nums[i]
    if d.get(x):
        d[x][1] += 1
    else:
        d[x] = [i, 1]
d = sorted(d.items(), key=lambda x: (-x[1][1], x[1][0]))
for k,v in d:
    print((str(k) + ' ') * v[1], end='')