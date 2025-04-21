#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n;

int test(int y, int x) {
    return (0 <= y && y < n && 0 <= x && x < n);
}

int main(void) {
    char op[256];
    scanf("%d\n", &n);

    char** arr = malloc(n * sizeof(char*));
    for (int i = 0; i < n; i++) {
        arr[i] = malloc(n * sizeof(char));
        memset(arr[i], '.', n);
    }

    fgets(op, sizeof(op), stdin);
    op[strcspn(op, "\r\n")] = '\0';

    int y = 0, x = 0;

    for (int i = 0; i < strlen(op); i++) {
        switch (op[i]) {
        case 'U':
            if (test(y - 1, x)) {
                if (arr[y][x] == '.') arr[y][x] = '|';
                else if (arr[y][x] == '-') arr[y][x] = '+';

                if (arr[y - 1][x] == '.') arr[y - 1][x] = '|';
                else if (arr[y - 1][x] == '-') arr[y - 1][x] = '+';

                y--;
            }
            break;
        case 'D':
            if (test(y + 1, x)) {
                if (arr[y][x] == '.') arr[y][x] = '|';
                else if (arr[y][x] == '-') arr[y][x] = '+';

                if (arr[y + 1][x] == '.') arr[y + 1][x] = '|';
                else if (arr[y + 1][x] == '-') arr[y + 1][x] = '+';

                y++;
            }
            break;
        case 'L':
            if (test(y, x - 1)) {
                if (arr[y][x] == '.') arr[y][x] = '-';
                else if (arr[y][x] == '|') arr[y][x] = '+';

                if (arr[y][x - 1] == '.') arr[y][x - 1] = '-';
                else if (arr[y][x - 1] == '|') arr[y][x - 1] = '+';

                x--;
            }
            break;
        case 'R':
            if (test(y, x + 1)) {
                if (arr[y][x] == '.') arr[y][x] = '-';
                else if (arr[y][x] == '|') arr[y][x] = '+';

                if (arr[y][x + 1] == '.') arr[y][x + 1] = '-';
                else if (arr[y][x + 1] == '|') arr[y][x + 1] = '+';

                x++;
            }
            break;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%c", arr[i][j]);
        }
        printf("\n");
        free(arr[i]);
    }
    free(arr);

    return 0;
}
