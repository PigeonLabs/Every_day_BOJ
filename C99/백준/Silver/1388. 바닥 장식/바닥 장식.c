#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void cnt(int n, int m, char arr[][m], int visited[][m], int i, int j, int o) {
    visited[i][j] = 1;
    if (o == 1) {
        if (i + 1 < n && arr[i + 1][j] == '|') {
            cnt(n, m, arr, visited, i + 1, j, o);
        }
    } else {
        if (j + 1 < m && arr[i][j + 1] == '-') {
            cnt(n, m, arr, visited, i, j + 1, o);
        }
    }
}

int main(void) {
    int n, m, o;
    scanf("%d %d", &n, &m);
    
    char grid[n][m];
    int visited[n][m];
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf(" %c", &grid[i][j]);
            visited[i][j] = 0;
        }
    }
    
    int res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (visited[i][j] == 1)
                continue;
            
            if (grid[i][j] == '|') {
                o = 1;
            } else if (grid[i][j] == '-') {
                o = 0;
            } else {
                continue;
            }
            cnt(n, m, grid, visited, i, j, o);
            res++;
        }
    }
    
    printf("%d", res);
    return 0;
}
