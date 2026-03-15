import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
x = eval('^'.join(map(str, d)))
if x == 0:
    print(0)
else:
    res = 0
    for i in d:
        if i^x <= i:
            res += 1
    print(res)