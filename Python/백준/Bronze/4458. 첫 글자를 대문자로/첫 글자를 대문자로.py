n = int(input())
for _ in range(n):
    t = list(input())
    if 'a' <= t[0] <= 'z':
        t[0] = chr(ord(t[0]) - 32)
    print("".join(t))