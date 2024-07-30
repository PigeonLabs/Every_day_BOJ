import sys
input = sys.stdin.readline
n, m = map(int, input().split())
al, bl = zip(*(map(int, input().split()) for _ in range(m)))
a = min(al)
b = min(bl)

print(min(a*((n+5)//6),a*(n//6)+b*(n%6),b*n))