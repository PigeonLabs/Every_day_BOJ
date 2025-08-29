#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int n, m;
int* arr, * list;

int cmp_asc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

void pt(int count, int start) {
    if (count == m) {
        for (int i = 0; i < m; i++) printf("%d ", list[i]);
        printf("\n");
        return;
    }
    for (int i = start; i < n; i++) {
        list[count] = arr[i];
        pt(count + 1, i);
    }
}

int main(void) {
    scanf("%d %d", &n, &m);

    arr = malloc(sizeof(int) * n);
    list = malloc(sizeof(int) * m);
    if (!arr || !list) return 1;

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    qsort(arr, n, sizeof(int), cmp_asc);

    pt(0, 0);

    free(list);
    free(arr);
    return 0;
}
