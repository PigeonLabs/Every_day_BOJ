#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int queen = 0;
    int w[8] = {0};
    int h[8] = {0};
    int c1[15] = {0};
    int c2[15] = {0};
    char ch;

    for (int i=0;i<8;i++) {
        for (int j=0;j<8;j++) {
            scanf(" %c", &ch);
            if (ch == '*') {
                if (h[i] == 0 && w[j] == 0 && c1[i + j] == 0 && c2[i - j + 7] == 0) {
                    h[i] = 1;
                    w[j] = 1;
                    c1[i + j] = 1;
                    c2[i - j + 7] = 1;
                    queen++;
                }
                else {
                    printf("invalid\n");
                    return 0;
                }
            }
        }
    }
    if (queen == 8) {
        printf("valid\n");
    }
    else {
        printf("invalid\n");
    }
    return 0;
}