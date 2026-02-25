from functools import cmp_to_key

def cmp(a,b):
    if a+b > b+a:
        return -1
    if a+b < b+a:
        return 1
    return 0

n = int(input())
arr = list(map(str, input().split()))

arr.sort(key=cmp_to_key(cmp))
if arr[0] == '0':
    print('0')
else:
    print(''.join(arr))