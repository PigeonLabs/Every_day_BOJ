key = input()
crypt = input()
length = len(crypt)//len(key)
crypt_split = [crypt[i:i+length] for i in range(0, len(crypt), length)]
res = [[0]for _ in range(len(key))]
en_key = sorted(list(enumerate(list(key))),key=lambda x : x[1])
for i in range(len(key)):
    res[en_key[i][0]] = crypt_split[i]

encrypt = ''.join(''.join(row) for row in [list(x) for x in zip(*res)])

print(encrypt)