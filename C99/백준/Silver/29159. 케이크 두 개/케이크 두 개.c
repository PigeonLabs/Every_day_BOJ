#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long long gcd(long long a, long long b) {
    long long tmp, x;
    if (a < b) {
        tmp = a;
        a = b;
        b = tmp;
    }
    while (b != 0) {
        x = a % b;
        a = b;
        b = x;
    }
    return a;
}

int main(void) {
    long long a, b, t;
    long long x1 = 0, x2 = 0, y1 = 0, y2 = 0, p1, p2, q1, q2;
    for (int i = 0; i < 4; i++) {
        scanf("%lld %lld", &a, &b);
        x1 += a;
        y1 += b;
    }
    for (int i = 0; i < 4; i++) {
        scanf("%lld %lld", &a, &b);
        x2 += a;
        y2 += b;
    }
    t = gcd(llabs(y2 - y1), llabs(x2 - x1));
    p1 = (y2 - y1) / t;
    p2 = (x2 - x1) / t;
    if (p2 < 0) {
        p1 = -p1;
        p2 = -p2;
    }
    if (p2 == 1) {
        printf("%lld ", p1);
    }
    else {
        printf("%lld/%lld ", p1, p2);
    }
    q1 = y1 * p2 - x1 * p1;
    q2 = 4 * p2;
    t = gcd(llabs(q1), llabs(q2));
    if (q2==t) {
        printf("%lld", q1/t);
    }
    else {
        printf("%lld/%lld", q1/t, q2/t);
    }
    return 0;
}