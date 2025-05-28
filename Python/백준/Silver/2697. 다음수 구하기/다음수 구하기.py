import sys
input = sys.stdin.readline

def next_permutation(a):
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i+1]:
        i -= 1
    if i < 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i+1:] = reversed(a[i+1:])
    return True

n = int(input())
for _ in range(n):
    digits = list(map(int, input().strip()))
    if not next_permutation(digits):
        print("BIGGEST")
    else:
        print("".join(map(str, digits)))
