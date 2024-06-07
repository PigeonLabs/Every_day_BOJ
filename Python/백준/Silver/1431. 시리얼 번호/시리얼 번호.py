l = []

def num(s):
    nl = []
    for i in s:
        if i.isdigit():
            nl.append(int(i))
    return nl

for i in range(int(input())):
    l.append(input())
res = sorted(l, key=lambda x: (len(x), sum(num(x)), x))
for ans in res:
    print(ans)