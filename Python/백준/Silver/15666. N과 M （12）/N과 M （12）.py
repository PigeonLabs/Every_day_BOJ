from itertools import combinations_with_replacement as cr

n,m = map(int,input().split())
for i in cr(sorted(set(map(int,input().split()))), m):
    print(*i)