#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) return 0;

    if (n == 1) {
        printf("1\n");
        return 0;
    }
    if (n == 2) {
        printf("1\n");
        return 0;
    }

    long long a = 1;
    long long b = 1;
    for (int i = 3; i <= n; ++i) {
        long long c = a + b;
        a = b;
        b = c;
    }
    printf("%lld\n", b);
    return 0;
}
