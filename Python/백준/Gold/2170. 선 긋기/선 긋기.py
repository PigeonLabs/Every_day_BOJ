import sys
input = sys.stdin.readline

n = int(input())
q = []
res = 0
for _ in range(n):
    q.append(tuple(map(int, input().split())))
q.sort()
s,e = q[0][0], q[0][1]
for a,b in q:
    if s <= a <= e:
        e = max(e,b)
    else:
        res += e-s
        s,e = a,b
print(res + e - s)