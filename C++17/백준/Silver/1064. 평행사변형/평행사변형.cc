#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#define min(x, y) (x) < (y) ? (x) : (y)
#define max(x, y) (x) > (y) ? (x) : (y)

int main(void) {
	double l[6];
	for (int i = 0; i < 6; i++) {
		scanf("%lf", &l[i]);
	}
	if ((l[0] - l[2]) * (l[1] - l[5]) == (l[0] - l[4]) * (l[1] - l[3])) {
		printf("-1.0");
	}
	else {
		double ab, bc, ca;
		ab = sqrt((l[0] - l[2]) * (l[0] - l[2]) + (l[1] - l[3]) * (l[1] - l[3]));
		bc = sqrt((l[0] - l[4]) * (l[0] - l[4]) + (l[1] - l[5]) * (l[1] - l[5]));
		ca = sqrt((l[2] - l[4]) * (l[2] - l[4]) + (l[3] - l[5]) * (l[3] - l[5]));
		double tx = max(max(ab, bc), ca);
		double tn = min(min(ab, bc), ca);
		printf("%.15lf", 2 * (tx - tn));
	}
	return 0;
}