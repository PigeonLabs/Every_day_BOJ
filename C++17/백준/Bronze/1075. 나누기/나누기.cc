#include <stdio.h>

int main(void) {
    int n,f;
    scanf("%d", &n);
    scanf("%d", &f);
    n = n/100*100;
    for (int i=0;i<100;i++) {
        if ((n+i)%f==0) {
            printf("%02d\n",i);
            break;
        }
    }
    return 0;
}