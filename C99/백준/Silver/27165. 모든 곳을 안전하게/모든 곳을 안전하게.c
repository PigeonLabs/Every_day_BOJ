#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n, s = 0;
    scanf("%d", &n);
    int* arr = malloc(sizeof(int) * (n + 1));
    for (int i = 0; i <= n; ++i) {
        scanf("%d", &arr[i]);
        if (arr[i] == 1) ++s;
    }
    int x;
    scanf("%d", &x);

    if (s > 2) {
        puts("NO");
        free(arr);
        return 0;
    }

    for (int i = 0; i + x <= n; ++i) {
        int j = i + x;

        if (arr[i] == 0 || arr[i] == 2 || arr[j] == 0) continue;

        int e = s;
        if (arr[i] == 1) --e;
        if (arr[j] == 1) --e;

        if (e == 0) {
            puts("YES");
            printf("%d %d\n", i, j);
            free(arr);
            return 0;
        }
    }

    puts("NO");
    free(arr);
    return 0;
}
