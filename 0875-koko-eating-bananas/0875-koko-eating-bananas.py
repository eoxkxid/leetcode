class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            speed = (left + right) // 2

            # speed의 속도로 모든 바나나를 먹는 데 필요한 시간
            total_hours = 0

            for pile in piles:
                total_hours += (pile + speed - 1) // speed

            if total_hours <= h:
                # speed는 가능하지만 최소 속도인지 모르므로
                # speed도 후보에 남겨둔 채 왼쪽을 탐색한다.
                right = speed
            else:
                # speed로는 너무 느리므로 speed 이하를 모두 제거한다.
                left = speed + 1

        return left