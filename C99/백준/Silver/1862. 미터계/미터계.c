#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int p(int base, int exp) {
    int r = 1;
    for (int i = 0; i < exp; i++) {
        r *= base;
    }
    return r;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int temp = n;
    int res = 0, x = 0;
    while (temp > 0) {
        int t = temp%10;
        if (t>4) {
            res += (t-1) * p(9, x);
        }
        else {
            res += t * p(9, x);
        }
        temp /= 10;
        x++;
    }
    printf("%d\n", res);
    return 0;
}
