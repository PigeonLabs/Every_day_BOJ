import math
for i in open(0):
    D,V = map(int, i.split())
    if D:
        print(f"{(D**3 - 6*V/math.pi)**(1/3):.3f}")