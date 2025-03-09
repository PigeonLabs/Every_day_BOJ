#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define min(x, y) ((x) > (y) ? (y) : (x))

struct road {
    int s;
    int e;
    int l;
};

int cmp(const void* a, const void* b) {
    struct road* ra = (struct road*)a;
    struct road* rb = (struct road*)b;
    if (ra->s != rb->s)
        return ra->s - rb->s;
    return ra->e - rb->e;
}

int main(void) {
    int n, d;
    scanf("%d %d", &n, &d);

    struct road* roads = malloc(sizeof(struct road) * n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d %d", &roads[i].s, &roads[i].e, &roads[i].l);
    }

    qsort(roads, n, sizeof(struct road), cmp);

    int* dp = malloc(sizeof(int) * (d + 1));
    for (int i = 0; i <= d; i++) {
        dp[i] = i;
    }

    int idx = 0;
    for (int i = 0; i <= d; i++) {
        if (i > 0) {
            dp[i] = min(dp[i], dp[i - 1] + 1);
        }
        while (idx < n && roads[idx].s == i) {
            if (roads[idx].e <= d) {
                dp[roads[idx].e] = min(dp[roads[idx].e], dp[i] + roads[idx].l);
            }
            idx++;
        }
    }

    printf("%d\n", dp[d]);

    free(dp);
    free(roads);
    return 0;
}
