#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    int resa=-1,resb=-1,resc=0;
    int ta=0;
    while (c-ta*a>=0) {
        int tb=(c-ta*a)/b;
        if (resc<ta*a+tb*b) {
            resa = ta;
            resb = tb;
            resc = ta*a+tb*b;
        }
        else if (resc==ta*a+tb*b) {
            if (resa+resb<ta+tb) {
                resa = ta;
                resb = tb;
                resc = ta*a+tb*b;
            }
        }
        ta++;
    }
    printf("%d %d",resa+resb,c-resc);
    return 0;
}