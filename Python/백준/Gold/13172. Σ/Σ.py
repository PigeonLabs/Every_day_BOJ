import sys,math
input = sys.stdin.readline

n,s = [],[]
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    n.append(a)
    s.append(b)
lcm = math.lcm(*n)
d = []
for i in range(t):
    d.append(s[i]*lcm//n[i])
sd = sum(d)
m = 1000000007

print((sd*pow(lcm,m-2,mod=m))%m)