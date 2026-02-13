alphabet = {chr(i): 0 for i in range(65, 91)}

n = int(input())
w = []
for i in range(n):
    s = input()
    w.append(s)
    for c in range(len(s)):
        alphabet[s[c]] += 10**(len(s)-c-1)

x = 9
k,v = "",""
for i in sorted(alphabet.items(), key=lambda x: x[1], reverse=True):
    if alphabet[i[0]] == 0:
        break
    k += i[0]
    v += str(x)
    x -= 1

res = 0
for i in w:
    res += int(i.translate(str.maketrans(k, v)))
print(res)