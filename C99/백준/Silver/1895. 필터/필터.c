#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int calc(int** arr, int y, int x) {
    int num[9];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            num[i*3+j] = arr[y+i][x+j];
        }
    }
    qsort(num, 9, sizeof(int), cmp);
    return num[4];
}

int main(void) {
    int r,c,t;
    scanf("%d %d", &r, &c);
    int** arr = malloc(r * sizeof(int*));
    for (int i = 0; i < r; i++) {
        arr[i] = malloc(c * sizeof(int));
        for (int j = 0; j < c; j++) {
            scanf("%d", &arr[i][j]);
        }
    }
    scanf("%d", &t);
    int res = 0;
    for (int i = 0; i < r-2; i++) {
        for (int j = 0; j < c-2; j++) {
            if (calc(arr, i, j) >= t) {
                res++;
            }
        }
    }
    printf("%d\n", res);
    for (int i = 0; i < r; i++) {
        free(arr[i]);
    }
    free(arr);
    return 0;
}
