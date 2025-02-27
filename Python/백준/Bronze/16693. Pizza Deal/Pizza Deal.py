from math import pi
a = list(map(int, input().split()))
b = list(map(int, input().split()))
r1 = a[0] / a[1]
r2 = (b[0] ** 2) * pi / b[1]
print("Whole pizza" if r2 > r1 else "Slice of pizza")