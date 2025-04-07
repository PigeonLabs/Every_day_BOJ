l = [1, 1]
ps = [1, 2]
n = int(input())
if n == 1:
    print(1)
    exit()
while ps[-1] < n:
    l.append(l[-2] + l[-1])
    ps.append(l[-1] + ps[-1])
lo = n - ps[-2] - 1  
res = "10"
m = len(ps) - 2
while m > 0:
    if m == 1:
        if lo == 0:
            res += "0"
        else:
            res += "1"
        m = 0
    else:
        if lo < l[m]:
            res += "0"
            m -= 1
        else:
            res += "1"
            lo -= l[m]
            res += "0"
            m -= 2
print(res)