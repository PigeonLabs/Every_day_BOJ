#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define min(a,b) (((a) < (b)) ? (a) : (b))
#define max(a, b) (((a) > (b)) ? (a) : (b))

int main(void) {
    long long n, a, b, c, d;
    scanf("%lld", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld %lld %lld", &a, &b, &c, &d);
        long long arr[3] = { a, b, c };
        for (int j = 0; j < 2; j++) {
            for (int k = j + 1; k < 3; k++) {
                if (arr[j] > arr[k]) {
                    long long temp = arr[j];
                    arr[j] = arr[k];
                    arr[k] = temp;
                }
            }
        }
        a = arr[0];
        b = arr[1];
        c = arr[2];

        long long s = a + b + c - d;
        long long t1 = min(s / 3, a);
        long long t2 = t1;
        s -= t1;

        t1 = min(s / 2, b);
        printf("%lld\n", t1 * t2 * (s - t1));
    }

    return 0;
}
