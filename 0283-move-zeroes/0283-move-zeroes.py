class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = 0 # Position to place the next non-zero element

        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                zero_pos += 1
'''
1. Use a zero_pos pointer to track where the next non-zero should go.
2. Iterate through nums:
    - When a non-zero is found, swap it with the element at zero_pos.
    - Increment zero_pos so that the next non-zero value is place correctly.
3. O(n) time with O(1) space.
'''