import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    res = [0] * (n + 1)
    for x in list(map(str, input().split(","))):
        if "-" in x:   
            a,b = map(int, x.split("-"))
            if a <= b:
                if n < a:
                    continue
                if a <= n <= b:
                    res[a:] = [1] * (n - a + 1)
                else:
                    res[a:b+1] = [1] * (b - a + 1)
        else:
            if int(x) <= n:
                res[int(x)] = 1
    print(res.count(1))