#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct person {
    char name[20];
    int n1;
    int n2;
    int n3;
} person;

int compare(const void* a, const void* b) {
    person p1 = *(const person*)a;
    person p2 = *(const person*)b;
    
    if (p1.n1 < p2.n1) return 1;
    else if (p1.n1 > p2.n1) return -1;
    else {
        if (p1.n2 < p2.n2) return -1;
        else if (p1.n2 > p2.n2) return 1;
        else {
            if (p1.n3 < p2.n3) return 1;
            else if (p1.n3 > p2.n3) return -1;
            else {
                return strcmp(p1.name, p2.name);
            }
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    person* p = malloc(sizeof(person) * n);
    for (int i = 0; i < n; i++) {
        scanf("%s %d %d %d", p[i].name, &p[i].n1, &p[i].n2, &p[i].n3);
    }
    qsort(p, n, sizeof(person), compare);
    for (int i = 0; i < n; i++) {
        printf("%s\n", p[i].name);
    }
    free(p);
    return 0;
}
