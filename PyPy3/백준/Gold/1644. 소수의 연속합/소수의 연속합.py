def erat(n):
    s = [True]*(n+1)
    s[0] = s[1] = False
    
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            for j in range(i*i, n+1,i):
                s[j] = False

    return [0]+[i for i in range(n+1) if s[i]]

primes = erat(4000100)
for i in range(1,len(primes)):
    primes[i] += primes[i-1]

a,l,r,c = 0,0,0,0
n = int(input())
while primes[r]-primes[r-1]<=n:
    a = primes[r]-primes[l]
    if l==r or a<n:
        r += 1
    elif a>n:
        l += 1
    elif a==n:
        c += 1
        r += 1
        l += 1
print(c)