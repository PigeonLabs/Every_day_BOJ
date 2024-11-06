#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int lcm(int a, int b) {
    return (a / gcd(a, b)) * b;
}

int main(void) {
    int num[5];
    int res = 1000000000;
    for (int i=0;i<5;i++) {
        scanf("%d",&num[i]);
    }
    for (int i=0;i<3;i++) {
        for (int j=i+1;j<4;j++) {
            for (int k=j+1;k<5;k++) {
                int current_lcm = lcm(lcm(num[i], num[j]), num[k]);
                if (current_lcm < res) {
                    res = current_lcm;
                }
            }
        }
    }
    printf("%d",res);
    return 0;
}
