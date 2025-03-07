#define max(x, y) (x) > (y) ? (x) : (y) 

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int* arr = malloc(sizeof(int) * n);
    scanf("%d", &arr[0]);
    for (int i = 0; i < n-1; i++) {
        scanf("%d", &arr[i+1]);
    }
    int mx = arr[0];
    for (int i = 1; i < n; i++) {
        arr[i] = max(arr[i], arr[i] + arr[i - 1]);
        mx = max(mx, arr[i]);
    }
    printf("%d", mx);
    free(arr);
    return 0;
}