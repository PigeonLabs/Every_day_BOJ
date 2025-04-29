l = list(ord(c) for c in list(input().strip()))
s = len(l)
idx = 1

for i in range(s - 1):
    if l[i] < l[i + 1]:
        l = l[:i+1][::-1] + l[i+1:]
        l = l[:i+2][::-1] + l[i+2:]

l = l[::-1]
print(''.join(chr(n) for n in l))