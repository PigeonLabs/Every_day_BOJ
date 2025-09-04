#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int n, m;
int *num;
int pick[10001];

int cmp(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

void dfs(int start, int depth) {
    if (depth == m) {
        for (int i = 0; i < m; ++i) {
            if (i) putchar(' ');
            printf("%d", pick[i]);
        }
        putchar('\n');
        return;
    }

    for (int i = start; i < n; ++i) {
        pick[depth] = num[i];
        dfs(i + 1, depth + 1);
    }
}

int main(void) {
    scanf("%d %d", &n, &m);
    num = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) scanf("%d", &num[i]);

    qsort(num, n, sizeof(int), cmp);
    dfs(0, 0);

    free(num);
    return 0;
}
