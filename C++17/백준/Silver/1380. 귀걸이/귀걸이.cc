#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int sn = 1;
    while (1) {
        int n;
        scanf("%d", &n);
        if (n == 0) {
            return 0;
        }

        int arrn[101] = {0};
        char arr[101][61];
        for (int i = 1; i <= n; i++) {
            scanf(" %[^\n]", arr[i]);
        }
        int r;
        char t;
        for (int i = 0; i < 2 * n - 1; i++) {
            scanf("%d %c", &r, &t);
            arrn[r]++;
        }
        for (int i = 1; i <= n; i++) {
            if (arrn[i] % 2 == 1) {
                printf("%d %s\n", sn, arr[i]);
                break;
            }
        }
        sn++;
    }
}