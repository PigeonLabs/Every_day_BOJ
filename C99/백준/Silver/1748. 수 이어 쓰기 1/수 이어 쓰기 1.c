#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int res = 0;
    int k = n;
    int exponent = 0;
    while ((int)pow(10, exponent) <= n) {
        int power = (int)pow(10, exponent);
        int range = 9 * power;
        int take = (k < range) ? k : range;
        res += (exponent + 1) * take;
        k -= range;
        exponent++;
    }
    printf("%d", res);
    return 0;
}
