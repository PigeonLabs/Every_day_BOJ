#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int ans = 0;
    int s = 1, e = 1;
    int res = 0;

    while (1) {
        if (res >= n) {
            if (res == n) ans++;
            res -= s;
            s++;
        }
        else if (e > n) {
            break;
        }
        else {
            res += e;
            e++;
        }
    }

    printf("%d\n", ans);
    return 0;
}
