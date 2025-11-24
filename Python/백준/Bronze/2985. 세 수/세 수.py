a, b, c = map(int, input().split())

#더하기
if a+b == c:
    print(f'{a}+{b}={c}')
elif a == b+c:
    print(f'{a}={b}+{c}')
#빼기
elif a-b == c:
    print(f'{a}-{b}={c}')
elif a == b-c:
    print(f'{a}={b}-{c}')
#곱하기
elif a*b == c:
    print(f'{a}*{b}={c}')
elif a == b*c:
    print(f'{a}={b}*{c}')
#나누기
elif a/b == c:
    print(f'{a}/{b}={c}')
else:
    print(f'{a}={b}/{c}')