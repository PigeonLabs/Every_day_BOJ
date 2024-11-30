def fac(n):
    if n==1:return 1
    return n * fac(n-1)

while (n:=int(input()))!=0:
    print(fac(2*n)//(fac(n)*fac(n+1)))