a = 1
b = int(input())

res = [0]*10
c = 0

if b==1:
    res[1] += 1
    print(*res)
    exit()

while b>a:
    while b>a:
        if a%10==0:
            break
        for i in list(str(a)):
            res[int(i)] += 10**c
        a += 1
    if a==b:
        for i in str(a):
            res[int(i)] += 10**c
        break
    if b%10!=9:
        for _ in range(b-((b//10)*10-1)):
            for i in list(str(b)):
                res[int(i)] += 10**c
            b -= 1
    if a // 10 == b // 10:
        while a <= b:
            for ch in str(a):
                res[int(ch)] += 10**c
            a += 1
        break
    else:
        for i in range(10):
            res[i] += (b//10-a//10+1)*10**c
    a //= 10
    b //= 10
    c += 1

print(*res)