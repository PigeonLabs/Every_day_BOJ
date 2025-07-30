import sys
input = sys.stdin.readline

def calc(num, p):
    return sum(int(d)**p for d in str(num))

a, p = map(int, input().split())
seen = { a }
seq = [a]

while True:
    nxt = calc(seq[-1], p)
    if nxt in seen:
        break
    seen.add(nxt)
    seq.append(nxt)
print(seq.index(nxt))