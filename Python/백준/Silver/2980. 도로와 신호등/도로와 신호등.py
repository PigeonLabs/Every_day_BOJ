import sys
input = sys.stdin.readline

n,l = map(int, input().split())
pos = 0
time = 0
for i in range(n):
    d,r,g = map(int, input().split())
    time += d - pos
    pos = d
    t = time % (r + g)
    if t < r:
        time += r - t
print(time + l - pos)