#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define max(x, y) ((x) > (y) ? (x) : (y))

typedef struct team {
    int name;
    int* scores;
    int attempt;
    int time;
}Team;

int k;

int compare(const void* a, const void* b) {
    Team* A = (Team*)a;
    Team* B = (Team*)b;

    int sumA = 0, sumB = 0;
    for (int i = 1; i <= k; i++) {
        sumA += A->scores[i];
        sumB += B->scores[i];
    }

    if (sumA != sumB) return sumB - sumA;
    if (A->attempt != B->attempt) return A->attempt - B->attempt;
    return A->time - B->time;
}

int main(void) {
    int tc,n,t,m,id,q,s;
    scanf("%d", &tc);
    for (int x = 0;x < tc;x++) {
        scanf("%d %d %d %d", &n, &k, &t, &m);
        Team* arr = malloc(sizeof(Team) * (n + 1));
        for (int i = 1;i <= n; i++) {
            arr[i].scores = calloc(k + 1, sizeof(int));
            arr[i].name = i;
            arr[i].attempt = 0;
            arr[i].time = 10001;
        }
        for (int i = 0;i < m; i++) {
            scanf("%d %d %d", &id, &q, &s);
            arr[id].scores[q] = max(arr[id].scores[q], s);
            arr[id].attempt++;
            arr[id].time = i;
        }

        qsort(arr+1, n, sizeof(Team), compare);

        for (int i = 1;i <= n; i++) {
            if (arr[i].name == t) {
                printf("%d\n", i);
            }
        }

        for (int i = 1; i <= n; i++) {
            free(arr[i].scores);
        }
        free(arr);
    }
    return 0;
}
