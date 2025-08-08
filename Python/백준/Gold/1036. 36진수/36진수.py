import sys
input = sys.stdin.readline

def ctoi(c):
    o = ord(c)
    if 48 <= o <= 57:
        return o - 48
    return o - 55

def itoc(v):
    if v < 10:
        return chr(v + 48)
    return chr(v + 55)

def solution(n, q=36):
    if n == 0:
        return "0"
    out = []
    while n > 0:
        n, mod = divmod(n, q)
        out.append(itoc(mod))
    return ''.join(reversed(out))

N = int(input())
gain = [0] * 36
total = 0

for _ in range(N):
    word = input().strip().upper()
    w = 1
    for ch in reversed(word):
        d = ctoi(ch)
        total += d * w
        gain[d] += (35 - d) * w
        w *= 36

K = int(input())
gain.sort(reverse=True)
total += sum(gain[:K])

print(solution(total, 36))