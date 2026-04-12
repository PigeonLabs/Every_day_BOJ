import sys
input = sys.stdin.readline

n = int(input())
dict = {}
for _ in range(n):
    x = input()
    dict[x] = dict.get(x, 0) + 1
for _ in range(n-1):
    x = input()
    dict[x] -= 1
    if dict[x] == 0:
        del dict[x]
print(list(dict.keys())[0])