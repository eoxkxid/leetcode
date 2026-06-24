class NumArray:

    def __init__(self, nums: List[int]):
        # prefix[i]는 nums[0]부터 nums[i - 1]까지의 합
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        # nums[left]부터 nums[right]까지의 합
        return self.prefix[right + 1] - self.prefix[left]      


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)