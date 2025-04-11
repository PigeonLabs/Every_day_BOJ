#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {
    int n, t;
    char status[6];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &t);
        if (t & 1) {
            strcpy(status, "odd");
        } else {
            strcpy(status, "even");
        }
        printf("%d is %s\n", t, status);
    }
    return 0;
}
