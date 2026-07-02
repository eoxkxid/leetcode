class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            # 이전 값을 덮어쓰기 전에 임시로 새 값 계산
            candidates = (x, current_max * x, current_min * x)

            current_max = max(candidates)
            current_min = min(candidates)

            answer = max(answer, current_max)

        return answer