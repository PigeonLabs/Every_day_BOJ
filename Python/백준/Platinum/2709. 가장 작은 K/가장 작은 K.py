import sys
input = sys.stdin.readline

arr = [1]
stage = 1
v = 1
for stage in range(2, 21):
    p = 4 * (5 ** (stage - 2))
    for i in range(5):
        tv = v+i*p
        res = pow(2, tv, 10**stage)
        if set(str(res).zfill(stage)) <= {'1', '2'}:
            arr.append(tv)
            v = tv
            break

n = int(input())
for _ in range(n):
    k = int(input())
    print(arr[k-1])