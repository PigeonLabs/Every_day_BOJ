#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {
    int n, m;
    char res[16];
    while (scanf(" R%dC%d", &n, &m) == 2) {
        if (n == 0 && m == 0)
            break;

        int idx = 0;
        while (m > 0) {
            m--;
            res[idx++] = 'A' + (m % 26);
            m /= 26;
        }
        for (int i = 0; i < idx / 2; i++) {
            char tmp = res[i];
            res[i] = res[idx - 1 - i];
            res[idx - 1 - i] = tmp;
        }
        res[idx] = '\0';

        printf("%s%d\n", res, n);
    }

    return 0;
}
