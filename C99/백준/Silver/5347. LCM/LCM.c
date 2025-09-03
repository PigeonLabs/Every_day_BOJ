#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* primes_up_to_n(int n, int* count) {
    if (n < 2) { *count = 0; return NULL; }

    int* is_prime = (int*)malloc((n + 1) * sizeof(int));
    if (!is_prime) exit(1);
    memset(is_prime, 1, (n + 1) * sizeof(int));
    is_prime[0] = is_prime[1] = 0;

    for (int i = 2; (long long)i * i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = 0;
            }
        }
    }

    *count = 0;
    for (int i = 2; i <= n; i++) if (is_prime[i]) (*count)++;

    int* primes = NULL;
    if (*count > 0) {
        primes = (int*)malloc((*count) * sizeof(int));
        if (!primes) exit(1);
        int idx = 0;
        for (int i = 2; i <= n; i++) if (is_prime[i]) primes[idx++] = i;
    }

    free(is_prime);
    return primes;
}

int main(void) {
    int tc;
    scanf("%d", &tc);
    for (int _ = 0; _ < tc; _++) {
        long long a, b;
        scanf("%lld %lld", &a, &b);
        int mx = (a > b) ? a : b;
        long long t = 1;
        int count;
        int* primes = primes_up_to_n(mx, &count);
        int j = 0;
        while (j < count) {
            int p = primes[j];
            if (a % p == 0 && b % p == 0) {
                a /= p;
                b /= p;
                t *= p;
            } else {
                j++;
            }
        }
        printf("%lld\n", t*a*b);
        free(primes);
    }
    return 0;
}
