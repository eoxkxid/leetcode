class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # 왼쪽 절반이 정상적으로 정렬되어 있는 경우
            if nums[left] <= nums[mid]:
                # target이 왼쪽 정렬 구간에 포함되는 경우
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # 오른쪽 절반이 정상적으로 정렬되어 있는 경우
            else:
                # target이 오른쪽 정렬 구간에 포함되는 경우
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1