#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int n, m;
int arr[8];

int compare(const int* a, const int* b) {
    return(*a - *b);
}

void calc(int t, int res[]) {
    if (t == m) {
        for (int i = 0; i < m; i++) {
            printf("%d ", res[i]);
        }
        printf("\n");
        return;
    }
    for (int i = 0; i < n; i++) {
        res[t] = arr[i];
        calc(t + 1, res);
    }
}

int main(void) {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    qsort(arr, n, sizeof(int), compare);
    int res[8];
    calc(0, res);
    return 0;
}