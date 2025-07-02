def calc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n&1:
        return n//2 + 2*calc(n//2) + 1
    else:
        return n//2 + 2*calc(n//2)
    
a,b = map(int, input().split())
print(calc(b)-calc(a-1))