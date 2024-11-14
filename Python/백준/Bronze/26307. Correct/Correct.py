import sys
input = sys.stdin.readline

n,k = map(int,input().split())
print((n-9)*60+k)