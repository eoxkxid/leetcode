class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 누적합 0이 배열 시작 전 index -1에서 등장했다고 본다
        prefix_first_index = {0: -1}

        prefix_sum = 0
        max_length = 0

        for i, num in enumerate(nums):
            # 0은 -1로, 1은 +1로 처리한다
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            # 같은 누적합이 이전에 있었다면,
            # 그 사이 구간의 합은 0이다
            if prefix_sum in prefix_first_index:
                length = i - prefix_first_index[prefix_sum]
                max_length = max(max_length, length)
            else:
                # 가장 긴 길이를 구해야 하므로 처음 등장한 위치만 저장한다
                prefix_first_index[prefix_sum] = i

        return max_length