def fn(i):
    if i == 0:
        return
    fn(i - 1)
    print(i)
    fn(i - 1)

n = int(input())
print(2**n-1)
fn(n)
print(n)