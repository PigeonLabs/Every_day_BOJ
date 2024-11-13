#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int n, cc = 0;
    scanf("%d", &n);
    for (int x = 0; x < n; x++) {
        int nx, dif = 0;
        scanf("%d", &nx);
        int score[51];
        for (int t = 0; t < nx; t++) {
            scanf("%d", &score[t]);
        }
        for (int i = 0; i < nx - 1; i++) {
            for (int j = 0; j < nx - 1 - i; j++) {
                if (score[j] < score[j + 1]) {
                    int temp = score[j];
                    score[j] = score[j + 1];
                    score[j + 1] = temp;
                }
            }
        }
        for (int i = 0; i < nx - 1; i++) {
            int gap = score[i] - score[i + 1];
            if (gap > dif) {
                dif = gap;
            }
        }
        printf("Class %d\n", ++cc);
        printf("Max %d, Min %d, Largest gap %d\n", score[0], score[nx - 1], dif);  // Fixed the indexing
    }
    return 0;
}