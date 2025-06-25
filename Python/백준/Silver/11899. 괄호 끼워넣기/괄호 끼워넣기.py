a = list(input())
res = 0
count = 0
for i in a:
    if i == '(':
        count += 1
    else:
        if count > 0:
            count -= 1
        else:
            res += 1
print(res + count)