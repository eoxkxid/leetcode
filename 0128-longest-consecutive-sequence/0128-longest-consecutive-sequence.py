class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 중복 제거 + O(1) 평균 탐색을 위한 set
        num_set = set(nums)

        longest = 0

        for num in num_set:
            # num이 연속 수열의 시작점인 경우만 탐색
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # 연속된 다음 숫자가 존재하는 동안 길이 증가
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest