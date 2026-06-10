void reverse(int* nums, int left, int right) {
    while (left < right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;

        left++;
        right--;
    }
}

void rotate(int* nums, int numsSize, int k) {
    k %= numsSize;

    // 1. 전체 배열 뒤집기
    reverse(nums, 0, numsSize - 1);

    // 2. 앞쪽 k개 뒤집기
    reverse(nums, 0, k - 1);

    // 3. 뒤쪽 numsSize - k개 뒤집기
    reverse(nums, k, numsSize - 1);
}