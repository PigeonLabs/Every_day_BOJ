import sys,math
input = sys.stdin.readline
MOD = 10007

n = int(input())
if n<4:
    print(0)
    exit()
res = 0
for t in range(1,n//4+1):
    x = (math.comb(13,t)*math.comb(52-t*4,n-t*4))%MOD
    if t%2:
        res = (res + x) % MOD
    else:
        res = (res - x) % MOD
print(res)