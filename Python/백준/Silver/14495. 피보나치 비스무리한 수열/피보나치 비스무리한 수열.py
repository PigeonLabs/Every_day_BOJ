nfib = [0,1,1,1]
n = int(input())
for i in range(4, n+1):
    nfib.append(nfib[i-1] + nfib[i-3])
print(nfib[n])