import sys
input = sys.stdin.readline

n = int(input())
d = dict()
res = 0
for i in range(n):
    name = input().rstrip()
    if name not in d:
        d[name] = 1
    else:
        if i < 2*d[name]:
            res += 1
        d[name] += 1
print(res)