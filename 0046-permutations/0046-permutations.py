class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        path = []
        used = [False] * n

        def backtrack():
            # 모든 원소를 선택했으면 순열 완성
            if len(path) == n:
                result.append(path.copy())
                return

            for i in range(n):
                if used[i]:
                    continue

                # 선택
                path.append(nums[i])
                used[i] = True

                # 다음 자리 탐색
                backtrack()

                # 선택 취소: 호출 전 상태로 복원
                path.pop()
                used[i] = False

        backtrack()
        return result