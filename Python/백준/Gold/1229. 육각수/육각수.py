n = int(input())
if n == 11 or n == 26:
    print(6)
    exit()
dp = [7] * (n + 1)
sn = []
i = 1
while True:
    v = i*(2*i - 1)
    i += 1
    if v > n:
        break
    sn.append(v)
    dp[v] = 1
snset = set(sn)

if n<=130:
    d = 1
    while d <= n:
        for x in sn:
            t = d+x
            if t > n:
                break
            ans = min(dp[t], dp[d] + 1)
            if t >= 27:
                if ans > 5:
                    break
            dp[t] = ans
        d += 1
    print(dp[n])
else:
    if n in snset:
        print(1)
        exit()
    for h in sn:
        if n - h in snset:
            print(2)
            exit()
    for h1 in sn:
        for h2 in sn:
            if n - h1 - h2 in snset:
                print(3)
                exit()
    print(4)