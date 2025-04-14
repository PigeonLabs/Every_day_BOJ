#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int number;
    int score;
    int rank;
} Player;

int compare_desc(const void* a, const void* b) {
    Player* p1 = (Player*)a;
    Player* p2 = (Player*)b;
    return p2->score - p1->score;
}

int compare_number(const void* a, const void* b) {
    Player* p1 = (Player*)a;
    Player* p2 = (Player*)b;
    return p1->number - p2->number;
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);

    char** arr = malloc(sizeof(char*) * n);
    for (int i = 0; i < n; i++) {
        arr[i] = malloc(sizeof(char) * (m + 1));
    }

    Player players[9];
    int c = 0;

    for (int i = 0; i < n; i++) {
        scanf("%s", arr[i]);
        for (int j = 0; j < m; j++) {
            char ch = arr[i][j];
            if ('1' <= ch && ch <= '9') {
                players[c].number = ch - '0';
                players[c].score = j;
                c++;
                break;
            }
        }
    }

    qsort(players, c, sizeof(Player), compare_desc);

    players[0].rank = 1;
    int t = 1;
    for (int i = 1; i < c; i++) {
        if (players[i].score == players[i - 1].score) {
            players[i].rank = t;
        }
        else {
            players[i].rank = ++t;
        }
    }

    qsort(players, c, sizeof(Player), compare_number);

    for (int i = 0; i < c; i++) {
        printf("%d\n", players[i].rank);
    }

    for (int i = 0; i < n; i++) {
        free(arr[i]);
    }
    free(arr);

    return 0;
}
