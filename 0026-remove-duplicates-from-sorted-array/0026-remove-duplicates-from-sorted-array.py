class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0 # Edge case for empty list

        unique_index = 0 # Slow pointer tracking unique element position

        for i in range(1, len(nums)): # Fast pointer iterating through array
            if nums[i] != nums[unique_index]: # Found a new unique element
                unique_index += 1 # Move slow pointer forward
                nums[unique_index] = nums[i] # Overwrite with the new unique value
        
        return unique_index + 1 # The count of unique elements
