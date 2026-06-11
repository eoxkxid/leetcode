#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int* answer = (int*)malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;

    // 1. answer[i]에 nums[i] 왼쪽에 있는 모든 원소의 곱 저장
    int leftProduct = 1;

    for (int i = 0; i < numsSize; i++) {
        answer[i] = leftProduct;
        leftProduct *= nums[i];
    }

    // 2. 오른쪽 곱을 누적하면서 answer[i]에 곱해주기
    int rightProduct = 1;

    for (int i = numsSize - 1; i >= 0; i--) {
        answer[i] *= rightProduct;
        rightProduct *= nums[i];
    }

    return answer;
}