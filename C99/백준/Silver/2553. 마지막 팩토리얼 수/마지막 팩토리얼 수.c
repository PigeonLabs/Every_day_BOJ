#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int fact0(int n)
{
    int twos = 0, f = 1, c;
    for (int s = n; s; s /= 2) twos += s / 2;
    for (int s = n; s; s /= 5) twos -= s / 5;
    for (int i = 3;i <= n;i++) {
        c = i;
        while (c % 2 == 0) c /= 2;
        while (c % 5 == 0) c /= 5; f = (f * c) % 10;
    }
    while (twos--) f = (f * 2) % 10;
    return f;
}

int main()
{
    int n;
    scanf("%d", &n);
    printf("%d\n", fact0(n));
}