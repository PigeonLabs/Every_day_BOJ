#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

int n, count, num;
char arr[100000][21];
char sorted[100000][21];
char str[21];

void merge_sort(char a[][21], int m, int mid, int n) {
	int i = m;
	int j = mid + 1;
	int k = m;

	while (i <= mid && j <= n) {
		if (strcmp(a[i], a[j]) <= 0) {
			strcpy(sorted[k], a[i]);
			i++;
		}
		else {
			strcpy(sorted[k], a[j]);
			j++;
		}
		k++;
	}

	if (i > mid) {
		for (int t = j; t <= n; t++) {
			strcpy(sorted[k], a[t]);
			k++;
		}
	}
	else {
		for (int t = i; t <= mid; t++) {
			strcpy(sorted[k], a[t]);
			k++;
		}
	}

	for (int t = m; t <= n; t++) {
		strcpy(a[t], sorted[t]);
	}
	return;
}

void merge(char a[][21], int m, int n) {
	if (m < n) {
		int mid = (m + n) / 2;
		merge(a, m, mid);
		merge(a, mid + 1, n);
		merge_sort(a, m, mid, n);
	}
	return;
}

int main() {
	scanf("%d", &n);
	scanf("%s", str);
	for (int i = 1; i < n; i++) {
		scanf("%s", str);
		if (strcmp(str, "ENTER") != 0) {
			strcpy(arr[num], str);
			num++;
		}
		if (i == n - 1 || strcmp(str, "ENTER") == 0) {
			merge(arr, 0, num - 1);
			for (int j = 1; j <= num; j++) {
				if (strcmp(arr[j - 1], arr[j]) != 0 || j == num) {
					count++;
				}
			}
			num = 0;
		}
	}
	printf("%d", count);
}