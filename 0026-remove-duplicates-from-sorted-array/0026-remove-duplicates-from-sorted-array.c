int removeDuplicates(int* nums, int numsSize) {
    int write = 1;

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[write - 1]) {
            nums[write] = nums[i];
            write++;
        }
    }

    return write;
}