#include <stdio.h>

int main()
{
    int a_divisor = 0;
    long long mx = 0, mn = 1000001;

    int n;
    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        scanf("%d", &a_divisor);
        if(a_divisor > mx)
            mx = a_divisor;
        if(a_divisor < mn)
            mn = a_divisor;
    }

    printf("%lld\n", mx * mn);

    return 0;
}