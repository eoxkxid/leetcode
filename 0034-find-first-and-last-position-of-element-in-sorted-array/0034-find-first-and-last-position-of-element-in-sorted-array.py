class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def find_first_position() -> int:
            left = 0
            right = len(nums) - 1
            first_position = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    # target은 mid보다 오른쪽에 있다.
                    left = mid + 1

                elif nums[mid] > target:
                    # target은 mid보다 왼쪽에 있다.
                    right = mid - 1

                else:
                    # target을 찾았지만 첫 번째 위치인지 확실하지 않다.
                    first_position = mid

                    # 더 앞에 있는 target을 찾기 위해 왼쪽 탐색
                    right = mid - 1

            return first_position

        def find_last_position() -> int:
            left = 0
            right = len(nums) - 1
            last_position = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    # target은 mid보다 오른쪽에 있다.
                    left = mid + 1

                elif nums[mid] > target:
                    # target은 mid보다 왼쪽에 있다.
                    right = mid - 1

                else:
                    # target을 찾았지만 마지막 위치인지 확실하지 않다.
                    last_position = mid

                    # 더 뒤에 있는 target을 찾기 위해 오른쪽 탐색
                    left = mid + 1

            return last_position

        first_position = find_first_position()
        last_position = find_last_position()

        return [first_position, last_position]