#include <stdio.h>

int main() {
    while (1) {
        int a;
        scanf("%d", &a);
        if (a == 0) {
            break;
        }
        int res = 1;
        
        for (int i = 0; i < 2 * a; i++) {
            int n;
            scanf("%d", &n);
            if (i % 2 == 0) {
                res *= n;
            } else {
                res -= n;
            }
        }
        printf("%d\n", res);
    }
    return 0;
}
