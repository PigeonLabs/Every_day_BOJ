#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);
    char** arr = malloc(sizeof(char*) * n);
    for (int i = 0; i < n; i++) {
        arr[i] = malloc(sizeof(char) * n);
        for (int j = 0; j < n; j++) {
            scanf(" %c", &arr[i][j]);
        }
    }

    int res1 = 0, res2 = 0;
    for (int i = 0; i < n; i++) {
        int j = 0;
        while (j < n - 1) {
            if (arr[i][j] == '.' && arr[i][j + 1] == '.') {
                res1++;
                while (j < n && arr[i][j] == '.') j++;
            }
            else {
                j++;
            }
        }
    }
    for (int j = 0; j < n; j++) {
        int i = 0;
        while (i < n - 1) {
            if (arr[i][j] == '.' && arr[i + 1][j] == '.') {
                res2++;
                while (i < n && arr[i][j] == '.') i++;
            }
            else {
                i++;
            }
        }
    }

    printf("%d %d", res1, res2);

    for (int i = 0; i < n; i++) free(arr[i]);
    free(arr);

    return 0;
}
