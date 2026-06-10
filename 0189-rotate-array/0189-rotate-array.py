class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        nums를 오른쪽으로 k칸 회전시킨다.
        반환하지 않고 nums 자체를 수정해야 한다.
        """

        n = len(nums)
        k %= n

        def reverse(left: int, right: int) -> None:
            # left와 right가 만날 때까지 양쪽 원소를 교환
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 1. 전체 배열 뒤집기
        reverse(0, n - 1)

        # 2. 앞쪽 k개 뒤집기
        reverse(0, k - 1)

        # 3. 뒤쪽 n-k개 뒤집기
        reverse(k, n-1)
        