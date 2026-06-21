class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            # 두 수의 합이 target이면 1-based index로 반환
            if current_sum == target:
                return [left + 1, right + 1]

            # 합이 작으면 더 큰 값을 사용해야 하므로 left 이동
            if current_sum < target:
                left += 1

            # 합이 더 크면 더 작은 값을 사용해야 하므로 right 이동
            else:
                right -= 1