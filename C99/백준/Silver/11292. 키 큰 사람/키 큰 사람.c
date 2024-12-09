#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    while (1) {
        int n;
        scanf("%d", &n);
        if (n == 0) {
            return 0;
        }
        else {
            double res = -1.0;
            double* num = malloc(sizeof(double) * n);
            char** name = malloc(sizeof(char*) * n);

            for (int i = 0; i < n; i++) {
                name[i] = malloc(sizeof(char) * 20);
            }

            for (int i = 0; i < n; i++) {
                char nm[20];
                double t;
                scanf("%s %lf", nm, &t);
                strcpy(name[i], nm);
                num[i] = t;

                if (t > res) {
                    res = t;
                }
            }

            for (int i = 0; i < n; i++) {
                if (res == num[i]) {
                    printf("%s ", name[i]);
                }
            }
            printf("\n");

            for (int j = 0; j < n; j++) {
                free(name[j]);
            }
            free(name);
            free(num);
        }
    }
    return 0;
}