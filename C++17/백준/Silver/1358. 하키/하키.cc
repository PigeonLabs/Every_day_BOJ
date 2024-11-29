#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main(void) {
    double w,h,x,y,p;
    int xx,yy, res = 0;
    scanf("%lf %lf %lf %lf %lf", &w, &h, &x, &y, &p);
    for (int i = 0; i < p; i++) {
        scanf("%d %d",&xx,&yy);
        if (
            (x<=xx && xx<x+w)&&(y<=yy && yy<=y+h)
            ||
            pow(pow((x-xx),2)+pow((y+h/2-yy),2),0.5)<=h/2
            ||
            pow(pow((x+w-xx),2)+pow((y+h/2-yy),2),0.5)<=h/2
        ) {
            res += 1;
        }
    }
    printf("%d",res);
    return 0;
}