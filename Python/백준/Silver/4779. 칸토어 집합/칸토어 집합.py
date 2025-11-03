import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        t = '-'
        for i in range(n):
            t += " "*len(t)+t
        print(t)
    except:
        break