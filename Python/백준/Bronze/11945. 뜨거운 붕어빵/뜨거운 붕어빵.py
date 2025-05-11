import sys
input = sys.stdin.readline

n,m = map(int, input().split())
for _ in range(n):
    x = input().rstrip()
    print(x[::-1])