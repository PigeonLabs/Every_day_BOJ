#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
    int n;
    scanf("%d", &n);
    double dollar = 100.0;

    int prev_A, cur_A;
    scanf("%d", &prev_A);
    
    for (int i = 0; i < n - 1; i++) {
        scanf("%d", &cur_A);
        if (prev_A > cur_A) {
            dollar *= ((double)prev_A / cur_A);
        }
        prev_A = cur_A;
    }
    printf("%.2f", dollar);
    return 0;
}
