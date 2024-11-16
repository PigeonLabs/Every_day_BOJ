#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n1, m1;
    scanf("%d %d", &n1, &m1);

    int** arr1 = (int**)malloc(n1 * sizeof(int*));
    for (int i = 0; i < n1; i++) {
        arr1[i] = (int*)malloc(m1 * sizeof(int));
    }

    for (int i = 0; i < n1; i++) {
        for (int j = 0; j < m1; j++) {
            scanf("%d",&arr1[i][j]);
        }
    }

    int n2, m2;
    scanf("%d %d", &n2, &m2);

    int** arr2 = (int**)malloc(n2 * sizeof(int*));
    for (int i = 0; i < n2; i++) {
        arr2[i] = (int*)malloc(m2 * sizeof(int));
    }

    for (int i = 0; i < n2; i++) {
        for (int j = 0; j < m2; j++) {
            scanf("%d",&arr2[i][j]);
        }
    }

    int** res = (int**)malloc(n1 * sizeof(int*));
    for (int i = 0; i < n1; i++) {
        res[i] = (int*)malloc(m2 * sizeof(int));
    }

    for (int i = 0; i < n1; i++) {
        for (int j = 0; j < m2; j++) {
            int r = 0;
            for (int t = 0; t < n2; t++) {
                r += arr1[i][t]*arr2[t][j];
            }
            res[i][j] = r;
        }
    }

    for (int i = 0; i < n1; i++) {
        for (int j = 0; j < m2; j++) {
            printf("%d ",res[i][j]);
        }
        printf("\n");
    }

    return 0;
}