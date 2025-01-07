a,b,c,d = map(int,input().split())
print(min(abs(a+b-c-d),abs(a+c-b-d),abs(a+d-b-c),abs(b+c-a-d),abs(b+d-a-c),abs(c+d-a-b)))