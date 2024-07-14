a = input()
b = input()
l = []

for i in a:
    l.append(i)
    if len(l) >= len(b) and ''.join(l[-len(b):]) == b:
        del l[-len(b):]

res = ''.join(l)
if res == "":
    print("FRULA")
else:
    print(res)