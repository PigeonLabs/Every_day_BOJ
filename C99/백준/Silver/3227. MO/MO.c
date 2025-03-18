#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void game(int *arr, int player, int location, int board_size) {
    int i = location + 1;
    while (i < board_size && arr[i] != 0 && arr[i] != player) {
        i++;
    }
    if (i < board_size && arr[i] == player) {
        for (int x = location + 1; x < i; x++) {
            arr[x] = 0;
        }
    }

    i = location - 1;
    while (i >= 0 && arr[i] != 0 && arr[i] != player) {
        i--;
    }
    if (i >= 0 && arr[i] == player) {
        for (int x = location - 1; x > i; x--) {
            arr[x] = 0;
        }
    }
}

int main(void) {
    int p, n;
    scanf("%d %d", &p, &n);
    int board_size = p + 1;
    int *arr = calloc(board_size, sizeof(int));
    
    for (int i = 0; i < n; i++) {
        int t;
        scanf("%d", &t);
        if (i % 2 == 0) {
            arr[t] = 1;
            game(arr, 1, t, board_size);
        }
        else {
            arr[t] = 2;
            game(arr, 2, t, board_size);
        }
    }
    
    int res1 = 0, res2 = 0;
    for (int i = 0; i < board_size; i++) {
        if (arr[i] == 1) res1++;
        else if (arr[i] == 2) res2++;
    }
    printf("%d %d", res1, res2);
    free(arr);
    return 0;
}
