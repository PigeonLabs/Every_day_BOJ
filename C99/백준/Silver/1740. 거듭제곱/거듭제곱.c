#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long long power(long long a, int b) {
    long long x = 1;
    for (int i=0;i<b;i++) {
        x *= a;
    }
    return x;
}

int main(void) {
    long long n;
    long long res = 0;
    scanf("%lld",&n);
    int arr[50] = {0};
    int cnt = 0;
    while(n != 0){
		if(n%2 == 1) arr[cnt] = 1;
		n /= 2;
		cnt++; 
	}
    for(int i = cnt-1; i >= 0; i--){
		if(arr[i] == 1){
			res += power(3,i);
		}	
	}
    printf("%lld",res);
    return 0;
}