#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int n, v;
    char q;
    while (1) {
        scanf(" %d %c %d", &n, &q, &v);
        if (n==0 && q=='W' && v==0) {
            return 0;
        }
        if (q=='W') {
            if (n-v>=-200) {
                printf("%d\n",n-v);
            }
            else {
                printf("Not allowed\n");
            }
        }
        else {
            printf("%d\n",n+v);
        }
    }
    return 0;
}
