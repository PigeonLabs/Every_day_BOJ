n = int(input())
if n&1:
    print("*"*n)
    print(" "*((n-1)//2)+"*")
    for i in range(1,(n-1)//2+1):
        print(" "*((n-1)//2-i)+"*"+" "*(2*i-1)+"*")
else:
    print("I LOVE CBNU")