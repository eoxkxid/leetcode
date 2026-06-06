class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            # 가장 오른쪽 비트가 1인지 확인
            if n & 1:
                count += 1

            # 오른쪽으로 한 칸 이동
            n >>= 1

        return count