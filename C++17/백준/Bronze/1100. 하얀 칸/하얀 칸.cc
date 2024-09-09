#include <stdio.h>

int main() {
    int res = 0;
    for (int i=0; i<8; i++) {
        int t;
        if (i%2==0) {
            t = 0;
        }
        else {
            t = 1;
        }
        char chess[8];
        scanf("%s",chess);
        for (int j=t; j<8; j+=2) {
            if (chess[j]=='F') {
                res++;
            }
        }
    }
    printf("%d\n",res);
    return 0;
}