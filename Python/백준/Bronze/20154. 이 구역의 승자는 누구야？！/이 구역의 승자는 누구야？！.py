x = input().strip()

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = '32123333113133122212112221'
point = dict(zip(a, map(int, b)))

total = 0
for ch in x:
    if ch in point:
        total += point[ch]

if total % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")