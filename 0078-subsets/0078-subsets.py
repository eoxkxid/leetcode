class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []

        def backtrack(start):
            # 현재 path 자체가 하나의 부분집합
            result.append(path.copy())

            # start 이후의 원소를 하나씩 선택
            for i in range(start, len(nums)):
                # 선택
                path.append(nums[i])

                # 다음 원소부터 탐색
                backtrack(i + 1)

                # 선택 취소
                path.pop()

        backtrack(0)

        return result