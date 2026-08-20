class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # 0을 왼쪽으로 이동
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                # 1은 이미 올바른 가운데 영역에 있음
                mid += 1
            
            else: # nums[mid] == 2
                # 2를 오른쪽으로 이동
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

                # high에서 가져온 값은 아직 확인하지 않았으므로
                # mid는 증가시키지 않는다.                