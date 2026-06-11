from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # 1. answer[i]에 nums[i] 왼쪽에 있는 모든 원소의 곱 저장
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # 2. 오른쪽 곱을 누적하면서 answer[i]에 곱해주기
        right_product = 1
        for i in range(n - 1, -1, -1): # range(start, stop, step):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer