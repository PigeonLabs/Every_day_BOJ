#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int arr[n];
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int up = 1, down = 1;
    int upMax = 1, downMax = 1;

    for(int i = 1; i < n; i++){
        if(arr[i-1] <= arr[i]) {
            up++;
            if(up > upMax) upMax = up;
        } else {
            up = 1;
        }
        if(arr[i-1] >= arr[i]) {
            down++;
            if(down > downMax) downMax = down;
        } else {
            down = 1;
        }
    }

    int answer = (upMax > downMax) ? upMax : downMax;
    printf("%d\n", answer);

    return 0;
}