class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0

        # 모든 숫자를 XOR하면 두 번 등장한 숫자는 사라지고
        # 한 번만 등장한 숫자만 남는다.
        for num in nums:
            answer ^= num

        return answer