#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    int* bits = (int*)malloc(sizeof(int) * (n + 1));

    *returnSize = n + 1;

    bits[0] = 0;

    for (int i = 1; i <= n; i++) {
        bits[i] = bits[i >> 1] + (i & 1);
    }

    return bits;
}