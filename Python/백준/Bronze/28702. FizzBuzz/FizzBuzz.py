c = 3
for i in range(3):
    n = input()
    if n.isdigit():
        break
    c -= 1
if (int(n)+c)%15==0:
    print("FizzBuzz")
elif (int(n)+c)%5==0:
    print("Buzz")
elif (int(n)+c)%3==0:
    print("Fizz")
else:
    print(int(n)+c)