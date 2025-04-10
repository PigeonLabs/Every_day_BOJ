#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int n,a,b,res=0;
    scanf("%d", &n);

    int arr[200001] = { 0 };
    for (int i = 0;i < n;i++) {
        scanf("%d %d", &a, &b);
        if (arr[a] != b) {
            arr[a] = b;
        }
        else {
            res++;
        }
    }
    for (int i = 0;i < 200001;i++) {
        if (arr[i] == 1) {
            res++;
        }
    }
    printf("%d", res);
    return 0;
}
