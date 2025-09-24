#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    unsigned long long n;
    unsigned long long l = 0;
    unsigned long long r = 4294967296;
    scanf("%llu", &n);
    while (l < r) {
        unsigned long long mid = (l + r) / 2;
        if (mid * mid <= n) {
            l = mid + 1;
        }
        else {
            r = mid;
        }
    }
    if ((l - 1) * (l - 1) == n) {
        l--;
    }
    printf("%llu\n", l);
    return 0;
}