import sys, itertools
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(map(int, input().split()))
for i in sorted(set(itertools.combinations(a, m))):
    print(*i)