a,b,c = map(int, input().split())
m = int(input())
print((a**2*(b-m)+c**2*m)/b-m*(b-m))