#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))

int main(void) {
    int n, a, b;
    int arr[1002][3] = { 0 };
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &a, &b);
        arr[a][0] = b;
    }
    arr[1001][2] = arr[1001][0];
    for (int i = 1; i <= 1000; i++) {
        arr[i][1] = max(arr[i - 1][1], arr[i][0]);
    }

    for (int i = 1000; i >= 1; i--) {
        arr[i][2] = max(arr[i + 1][2], arr[i][0]);
    }

    int res = 0;
    for (int i = 1; i <= 1000; i++) {
        res += min(arr[i][1], arr[i][2]);
    }

    printf("%d\n", res);
    return 0;
}
