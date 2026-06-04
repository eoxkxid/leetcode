int singleNumber(int* nums, int numsSize) {
    int answer = 0;

    for (int i = 0; i < numsSize; i++) {
        // 같은 숫자는 XOR하면 0이 되고,
        // 0과 XOR한 값은 자기 자신이 된다.
        answer ^= nums[i];
    }

    return answer;
}