while True:
    n = int(input())
    if n==-1:
        break
    res = 0
    p = 0
    for _ in range(n):
        a,b = map(int,input().split())
        res += a*(b-p)
        p = b
    print(res,"miles")