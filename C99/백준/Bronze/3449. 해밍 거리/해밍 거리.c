#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {
    int n, res = 0;
    char a[101], b[101];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", &a);
        scanf("%s", &b);
        res = 0;
        for (int x = 0; x < strlen(a); x++) {
            if (a[x] != b[x]) res++;
        }
        printf("Hamming distance is %d.\n", res);
    }
    return 0;
}
