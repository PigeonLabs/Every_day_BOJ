#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int t = 1;
    while (1) {
        int n, s1, s2, s3, s4;
        scanf("%d", &n);
        if (n == 0) {
            break;
        }
        int** arr = malloc(sizeof(int*) * n);
        int* num = calloc(1024, sizeof(int));
        int arrsum[2][8];

        for (int i = 0; i < n; i++) {
            arr[i] = malloc(sizeof(int) * n);
            for (int j = 0; j < n; j++) {
                scanf("%d", &arr[i][j]);
                num[arr[i][j]]++;
            }
        }

        printf("Square %d: ", t++);

        s3 = 0;
        s4 = 0;
        for (int i = 0; i < n; i++) {
            s1 = 0;
            s2 = 0;
            for (int j = 0; j < n; j++) {
                s1 += arr[i][j];
                s2 += arr[j][i];
            }
            arrsum[0][i] = s1;
            arrsum[1][i] = s2;
            s3 += arr[i][i];
            s4 += arr[i][n - i - 1];
        }

        int x = arrsum[0][0];
        int non = 0;
        for (int i = 0; i < n; i++) {
            if (x != arrsum[0][i] || x != arrsum[1][i]) {
                non = 1;
                break;
            }
        }
        if (non) {
            printf("Not a Magick Square\n");
            continue;
        }
        if (x != s3 || x != s4) {
            printf("Semi-Magick Square\n");
            continue;
        }
        int weak = 0;
        for (int i = 0; i < 1024; i++) {
            if (1 < num[i]) {
                weak = 1;
                break;
            }
        }
        if (weak) {
            printf("Weakly-Magick Square\n");
            continue;
        }

        int min = -1, max = -1, consecutive = 1;
        for (int i = 1; i <= n * n; i++) {
            if (num[i] > 0) {
                if (min == -1) {
                    min = i;
                }
                max = i;
            }
        }

        if (max - min == n * n - 1) {
            printf("Magically-Magick Square\n");
        }
        else {
            printf("Strongly-Magick Square\n");
        }

        // Free memory
        for (int i = 0; i < n; i++) {
            free(arr[i]);
        }
        free(arr);
        free(num);
    }

    return 0;
}
