#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int h1, m1, s1, h2, m2, s2, rh, rm, rs;
	for (int i = 0; i < 3; i++) {
		scanf("%d %d %d %d %d %d", &h1, &m1, &s1, &h2, &m2, &s2);
		if (s2>=s1) {
			rs = s2 - s1;
		}
		else {
			rs = 60 + s2 - s1;
			m2--;
		}
		if (m2 >= m1) {
			rm = m2 - m1;
		}
		else {
			rm = 60 + m2 - m1;
			h2--;
		}
		printf("%d %d %d\n", h2 - h1, rm, rs);
	}
	return 0;
}