class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 오름차순으로 정렬했을 때 찾아야 하는 인덱스
        # 오름차순으로 정렬했을 때 찾아야 하는 인덱스
        target_index = len(nums) - k

        left = 0
        right = len(nums) - 1

        while left <= right:
            # 특정 입력에서 최악의 경우가 반복되는 것을 줄이기 위해
            # 현재 탐색 범위에서 피벗을 무작위로 선택한다.
            pivot = nums[random.randint(left, right)]

            # 분할 후 만들어질 영역
            # [left, less - 1]    : pivot보다 작은 값
            # [less, greater]     : pivot과 같은 값
            # [greater + 1, right]: pivot보다 큰 값
            less = left
            current = left
            greater = right

            while current <= greater:
                if nums[current] < pivot:
                    nums[less], nums[current] = nums[current], nums[less]
                    less += 1
                    current += 1

                elif nums[current] > pivot:
                    nums[current], nums[greater] = (
                        nums[greater],
                        nums[current],
                    )
                    greater -= 1

                    # 뒤에서 가져온 값은 아직 확인하지 않았으므로
                    # current는 증가시키지 않는다.

                else:
                    current += 1

            # target이 pivot보다 작은 값들의 영역에 있는 경우
            if target_index < less:
                right = less - 1

            # target이 pivot보다 큰 값들의 영역에 있는 경우
            elif target_index > greater:
                left = greater + 1

            # target이 pivot과 같은 값들의 영역에 있는 경우
            else:
                return nums[target_index]