import sys
input = sys.stdin.readline

def pf(n):
    l = dict()
    i = 2
    while n!=1:
        if n%i==0:
            l[i] = l.get(i,0)+1
            n //= i
        else:
            i += 1
    return l

for _ in range(int(input())):
    for i,k in pf(int(input())).items():
        print(i,k)