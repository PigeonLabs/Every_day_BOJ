import math

def eratos(n):
    prime = [True for i in range(n+1)]
    prime[0] = prime[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        if prime[i] == True:
            j = 2
            while i*j <= n:
                prime[i*j] = False
                j += 1
    return prime

n = int(input())
p = eratos(n)
res = 1
for i in range(2,n+1):
    if p[i]:
        t = 1
        while i**(t+1)<=n:
            t += 1
        res = (res * pow(i, t, 987654321)) % 987654321
print(res)