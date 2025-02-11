class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

''' 
이진 탐색(Binary Search)
1. left, right 두 포인터를 설정하여 이진 탐색 수행
2. mid를 계산하고 nums[mid]와 target 비교
3. 찾지 못한 경우, left가 target이 삽입될 위치
'''