import math

def score(r, sig):
    return 1-pow(math.e,-r**2/(2*sig**2))

n1,n2,n3,n4,n5,n6 = map(float, input().split())
sig = float(input())
print((score(n6,sig)*2-score(n5,sig)+score(n4,sig)*2-score(n3,sig)*2-score(n2,sig))*10.5+(score(n2,sig)+score(n1,sig))*25)