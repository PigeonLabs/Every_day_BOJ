import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

pi = [0] * n
j = 0

for i in range(1, n):
    while j > 0 and s[i] != s[j]:
        j = pi[j - 1]
    if s[i] == s[j]:
        j += 1
        pi[i] = j

print(n - pi[-1])