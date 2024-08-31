from functools import cache

n,p,q = map(int,input().split())

@cache
def seq(i):
    if not i:
        return 1
    return seq(int(i/p))+seq(int(i/q))

print(seq(n))