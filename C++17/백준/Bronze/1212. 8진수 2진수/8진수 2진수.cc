#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
    char n[333334];
    int s = 0,a = 0;
    scanf("%s",n);

    if (strcmp(n, "0") == 0) {
        printf("0");
        return 0;
    }

    int length = strlen(n);
    for (int i = 0;i<length;i++) {
        int t = n[i] - '0';
        int x = 4;
        while (x>0) {
            if (t>=x) {
                printf("1");
                t -= x;
                a = 1;
            }
            else if (a) {
                printf("0");
            }
            x /= 2;
        }
    }
    return 0;
}