#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    for (int tc = 1; tc <= n; tc++) {
        int p, q;
        scanf("%d %d", &p, &q);
        long long a = 1 % q, b = 1 % q, c = 0;
        if (p == 1) {
            c = a;
        }
        else {
            for (int j = 2; j < p; j++) {
                c = (a + b) % q;
                a = b;
                b = c;
            }
            c = b;
        }

        printf("Case #%d: %lld\n", tc, c);
    }
    return 0;
}
