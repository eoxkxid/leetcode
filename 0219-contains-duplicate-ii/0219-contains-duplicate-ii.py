from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i, num in enumerate(nums):
            # 이전에 같은 숫자가 나온 적 있는 경우
            if num in last_seen:
                # 현재 인덱스와 이전 인덱스의 차이가 k 이하인지 확인
                if i - last_seen[num] <= k:
                    return True

            # 현재 숫자의 가장 최근 위치 갱신
            last_seen[num] = i

        return False