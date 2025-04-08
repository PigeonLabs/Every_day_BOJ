#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    long long a,b;
    scanf("%lld %lld", &a, &b);
    if (a > b) {
        long long temp = a;
        a = b;
        b = temp;
    }
    printf("%lld", (b - a + 1) * (a + b) / 2);
    return 0;
}