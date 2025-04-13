#include <stdio.h>
int main() {
    int c, n, m;
    scanf("%d %d %d", &c, &n, &m);
    int ans = (c*n)-m;
    if (ans > 0)
        printf("%d", ans);
    else
        printf("0");
    return 0;
}