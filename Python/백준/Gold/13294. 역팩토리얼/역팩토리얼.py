from math import log

n = int(input())
nl = log(n)
s = 1
while (s*log(s)-s+.5*log(2*3.141592653589793*s)) < nl:
    s += 1

print(s-1)