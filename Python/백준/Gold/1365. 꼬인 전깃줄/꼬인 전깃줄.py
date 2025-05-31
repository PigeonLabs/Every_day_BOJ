import sys,bisect
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l2 = l[::-1]
d = [[l[0],1]]
d2 = [[l2[0],1]]
for i in range(1,n):
    if d[-1][0] < l[i]:
        d.append([l[i],1])
    else:
        idx = bisect.bisect_left(d, [l[i],0])
        if d[idx][0] == l[i]:
            d[idx][1] += 1
        else:
            d[idx] = [l[i],1]
    if d2[-1][0] < l2[i]:
        d2.append([l2[i],1])
    else:
        idx = bisect.bisect_left(d2, [l2[i],0])
        if d2[idx][0] == l2[i]:
            d2[idx][1] += 1
        else:
            d2[idx] = [l2[i],1]
res1, res2 = 0,0
for i in d:
    res1 += i[1]
    res2 += i[1]
print(n - max(res1,res2))