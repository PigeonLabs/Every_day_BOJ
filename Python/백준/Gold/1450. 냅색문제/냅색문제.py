import sys,itertools,bisect
input = sys.stdin.readline

n,c = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
v1 = v[:n//2]
v2 = v[n//2:]
l1,l2 = [0],[0]
for i in range(len(v1)):
    for t in itertools.combinations(v1, i+1):
        l1.append(sum(t))
for i in range(len(v2)):
    for t in itertools.combinations(v2, i+1):
        l2.append(sum(t))
l2.sort()

res = 0
for i in l1:
    if i > c:
        continue
    idx = bisect.bisect_right(l2,c-i)
    res += idx
print(res)