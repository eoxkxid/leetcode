class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)

        for i in range(1, n + 1):
            # i >> 1은 i // 2와 같고,
            # i & 1은 i가 홀수인지 확인하는 값이다.
            bits[i] = bits[i >> 1] + (i & 1)

        return bits