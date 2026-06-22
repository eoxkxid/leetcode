class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height

            max_area = max(max_area, current_area)

            # 더 낮은 쪽이 물의 높이를 제한하므로 그쪽 포인터를 이동한다.
            # 더 높은 쪽의 포인터를 옮기는 것은 의미가 없다
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area