w = input()
f = input()
i = 0
start = 0

while (a := w.find(f, start)) != -1:
    w = w[:a] + w[a + len(f):]
    i += 1
    start = a

print(i)