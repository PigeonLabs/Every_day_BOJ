from itertools import permutations as p
n,m = map(int,input().split())
l = list(map(int,input().split()))
for i in sorted(set(p(l,m))):
    print(*i)