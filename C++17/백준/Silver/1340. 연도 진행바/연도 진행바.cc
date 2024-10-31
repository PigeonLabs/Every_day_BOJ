# define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

struct Month {
    char name[10];
    int days;
};

int main(void) {
    struct Month months[12] = {
        {"January", 31},
        {"February", 28},
        {"March", 31},
        {"April", 30},
        {"May", 31},
        {"June", 30},
        {"July", 31},
        {"August", 31},
        {"September", 30},
        {"October", 31},
        {"November", 30},
        {"December", 31}
    };

    char m[20];
    
    int d,y,t1,t2;
    int ly,fday,lday = 0;
    scanf("%s %d, %d %d:%d",m,&d,&y,&t1,&t2);

    if (y%400==0) {
        ly = 1;
    }
    else if (y%100==0) {
        ly = 0;
    }
    else if (y%4==0) {
        ly = 1;
        
    }
    else {
        ly = 0;
    }

    if (ly) {
        months[1].days = 29;
        fday = 366;
    }
    else {
        fday = 365;
    }

    lday += d-1;
    for (int i = 0; i < 12; i++) {
        if (strcmp(m, months[i].name) != 0) {
            lday += months[i].days;
        }
        else {
            break;
        }
    }

    double res = ((double)lday + (double)t1 / 24.0 + ((double)t2 / 1440.0)) * 100.0 / (double)fday;

    printf("%.15lf\n",res);

    return 0;
}