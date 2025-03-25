#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define INF 100001
#define min(x, y) ((x) < (y) ? (x) : (y))

int *coin;
int **memo;

int solve(int n, int k) {
    if (k == 0) {
        return 0;
    }
    if (n < 0) {
        return INF;
    }
    if (memo[n][k] != -1) {
        return memo[n][k];
    }
    
    int c1 = INF, c2 = INF;
    if (coin[n] <= k) {
        c1 = 1 + solve(n, k - coin[n]);
    }
    c2 = solve(n - 1, k);
    memo[n][k] = min(c1, c2);
    return memo[n][k];
}

int main(void) {
    int n, k;
    scanf("%d %d", &n, &k);
    
    coin = (int*)malloc(sizeof(int) * n);
    memo = (int**)malloc(sizeof(int*) * n);
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &coin[i]);
    }
    
    for (int i = 0; i < n; i++) {
        memo[i] = (int*)malloc(sizeof(int) * (k + 1));
        for (int j = 0; j <= k; j++) {
            memo[i][j] = -1;
        }
    }
    
    int ans = solve(n - 1, k);
    if (ans >= INF) {
        printf("%d", -1);
    } else {
        printf("%d", ans);
    }
    
    for (int i = 0; i < n; i++) {
        free(memo[i]);
    }
    free(memo);
    free(coin);
    return 0;
}
