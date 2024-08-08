n, b = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

def mat_mult(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(n)) % 1000
    return result

result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
power = l.copy()

while b > 0:
    if b % 2 == 1:
        result = mat_mult(result, power)
    power = mat_mult(power, power)
    b //= 2

for row in result:
    print(' '.join(map(str, row)))
