n = list(input())

res = 0
for i in range(12):
    if n[i] == '*':
        r = i
        continue
    res += int(n[i]) * (1 if i % 2 == 0 else 3)

c = int(n[12])
q = 1 if r % 2 == 0 else 3
need = (10 - ((res + c) % 10)) % 10
if q == 1:
    x = need
else:
    x = (7 * need) % 10
print(x)