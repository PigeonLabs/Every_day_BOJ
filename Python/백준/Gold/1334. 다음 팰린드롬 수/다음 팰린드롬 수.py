n = int(input())+1

t = list(map(int, str(n)))

def decal(t):
    for i in range(len(t)//2):
        t[-i-1] = t[i]

def validation(t):
    if len(t)&1:
        for i in range(10):
            t[len(t)//2] = i
            res = int("".join(map(str, t)))
            if res>=n:
                print(res)
                return True
    else:
        res = int("".join(map(str, t)))
        if res>=n:
            print(res)
            return True
    return False

def plus(t, k):
    while k >= 0:
        if t[k] < 9:
            t[k] += 1
            return
        else:
            t[k] = 0
            k -= 1
    t.insert(0, 1)

decal(t)
while True:
    if validation(t):
        break
    else:
        if len(t)&1:
            plus(t,len(t)//2)
            decal(t)
        else:
            plus(t,len(t)//2-1)
            t[len(t)//2] = t[len(t)//2-1]
            decal(t)