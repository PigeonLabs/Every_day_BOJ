import math

n = int(input())
t = (math.isqrt(8*n+1)-1)//2
print((pow(2,t,9901)*(n%9901-1-(t*(t-1)//2)%9901)+1)%9901)