#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long tmp = b;
        b = a % b;
        a = tmp;
    }
    return a;
}

int main() {
    long long g, l;
    scanf("%lld %lld", &g, &l);

    long long k = l / g;
    long long x, y;
    long long min_sum = 1LL << 62;
    long long ans_a = 0, ans_b = 0;

    for (long long i = 1; i * i <= k; i++) {
        if (k % i == 0) {
            x = i;
            y = k / i;
            if (gcd(x, y) == 1) {
                long long a = g * x;
                long long b = g * y;
                if (a + b < min_sum) {
                    min_sum = a + b;
                    if (a < b) {
                        ans_a = a;
                        ans_b = b;
                    }
                    else {
                        ans_a = b;
                        ans_b = a;
                    }
                }
            }
        }
    }

    printf("%lld %lld\n", ans_a, ans_b);
    return 0;
}
