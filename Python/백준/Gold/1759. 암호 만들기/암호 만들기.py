import sys
input = sys.stdin.readline
from itertools import combinations as cb

n,m = map(int, input().split())
l = map(str, input().split())
con = []
vow = []
res = []
for i in l:
    if i in ["a","e","i","o","u"]:
        vow.append(i)
    else:
        con.append(i)
for t in range(1,len(vow)+1):
    if t+2<=n:
        for i in list(cb(vow,t)):
            for j in list(cb(con,n-t)):
                res.append(sorted(i+j))
for r in sorted(res):
    print("".join(r))