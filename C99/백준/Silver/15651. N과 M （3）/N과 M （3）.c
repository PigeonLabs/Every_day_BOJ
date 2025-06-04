#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int n, m;
int arr[7];

void solve(int count) {
	if (count == m) {
		for (int i = 0; i < m; i++) {
			printf("%d ", arr[i]);
		}
		printf("\n");
		return;
	}
	for (int i = 1; i <= n; i++) {
		arr[count] = i;
		solve(count + 1);
	}
}

int main(void) {
	scanf("%d %d", &n, &m);
	solve(0);
	return 0;
}