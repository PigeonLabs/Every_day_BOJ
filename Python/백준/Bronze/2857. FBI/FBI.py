import sys
input = sys.stdin.readline

name = [input() for _ in range(5)]
res = False
for i in name:
    if 'FBI' in i:
        print(name.index(i)+1, end=' ')
        res = True
if not res:
    print('HE GOT AWAY!')