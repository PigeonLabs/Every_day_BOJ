a = list(input())
b = list(input())
al,bl = len(a),len(b)
l = [[0 for _ in range(bl+1)]for _ in range(al+1)]
for i in range(1,al+1):
    for j in range(1,bl+1):
        if a[i-1]==b[j-1]:
            l[i][j] = l[i-1][j-1]+1
        else:
            l[i][j] = max(l[i-1][j],l[i][j-1])
resl = l[-1][-1]

lcs = []
while al > 0 and bl > 0:
    if a[al - 1] == b[bl - 1]:
        lcs.append(a[al - 1])
        al -= 1
        bl -= 1
    elif l[al-1][bl] >= l[al][bl-1]:
        al -= 1
    else:
        bl -= 1

if resl:
    print(resl)
    print("".join(reversed(lcs)))
else:
    print(0)