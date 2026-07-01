class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # 현재 숫자부터 새로 시작할지, 이전 부분 배열에 붙일지 선택
            current_sum = max(nums[i], current_sum + nums[i])

            # 지금까지 본 부분 배열 합 중 최댓값 갱신
            max_sum = max(max_sum, current_sum)

        return max_sum