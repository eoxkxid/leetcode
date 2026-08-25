class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k번째로 큰 값은 오름차순 기준으로 인덱스 len(nums) - k에 위치한다.
        # 실제로 배열 전체를 정렬하지 않고, 해당 위치의 값만 찾는다.
        target_index = len(nums) - k

        # 현재 정답을 탐색할 인덱스 범위
        left = 0
        right = len(nums) - 1

        while left <= right:
            # 편향된 입력에서 나쁜 피벗이 반복되는 가능성을 줄이기 위해
            # 현재 탐색 범위에서 피벗 값을 무작위로 선택한다.
            pivot = nums[random.randint(left, right)]

            # 반복 중 배열 영역의 의미
            # [left, less - 1]      : pivot보다 작은 값
            # [less, current - 1]   : pivot과 같은 값
            # [current, greater]    : 아직 확인하지 않은 값
            # [greater + 1, right]  : pivot보다 큰 값
            less = left
            current = left
            greater = right

            while current <= greater:
                if nums[current] < pivot:
                    # 현재 작은 값을 왼쪽의 작은 값 영역으로 이동한다.
                    nums[less], nums[current] = (
                        nums[current],
                        nums[less],
                    )

                    # 작은 값 영역이 한 칸 늘어난다.
                    less += 1

                    # current 위치로 들어온 값은 이미 확인된 pivot 값이므로
                    # 다음 원소로 이동한다.
                    current += 1

                elif nums[current] > pivot:
                    # 현재 큰 값을 오른쪽의 큰 값 영역으로 이동한다.
                    nums[current], nums[greater] = (
                        nums[greater], 
                        nums[current],
                    )

                    # 큰 값 영역이 한 칸 늘어난다.
                    greater -= 1

                    # 오른쪽에서 current 위치로 가져온 값은 아직 확인하지 않았으므로
                    # current는 증가시키지 않는다.

                else:
                    # 현재 값이 pivot과 같으므로 같은 값 영역을 한 칸 늘린다.
                    current += 1

            # 분할 종료 후:
            # [left, less - 1]      : pivot보다 작은 값
            # [less, greater]       : pivot과 같은 값
            # [greater + 1, right]  : pivot보다 큰 값

            if target_index < less:
                # 목표 인덱스가 pivot 동일 영역보다 왼쪽에 있으므로
                # 왼쪽 영역만 다시 탐색한다.
                right = less - 1

            elif target_index > greater:
                # 목표 인덱스가 pivot 동일 역역보다 오른쪽에 있으므로
                # 오른쪽 영역만 다시 탐색한다.
                left = greater + 1

            else:
                # 목표 인덱스가 pivot과 같은 값들의 영역 안에 있다.
                return nums[target_index]

                