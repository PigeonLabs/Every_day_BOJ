from collections import Counter

def counter(s):
    d = Counter()
    for i in range(len(s)):
        if s[i].isupper():
            d[s[i]] += 1
        elif s[i].isdigit():
            d[s[i-1]] += int(s[i]) - 1
    return d

def mul(cnt, x):
    return Counter({k: v * x for k, v in cnt.items()})

a, b, c = input().replace('=', '+').split('+')

a = counter(a)
b = counter(b)
c = counter(c)

for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            if mul(a, i) + mul(b, j) == mul(c, k):
                print(i, j, k)
                exit()