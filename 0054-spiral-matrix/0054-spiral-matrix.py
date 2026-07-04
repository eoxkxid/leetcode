class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. 위쪽 행: 왼쪽 -> 오른쪽
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # 2. 오른쪽 열: 위 -> 아래
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # 3. 아래쪽 행: 오른쪽 -> 왼쪽
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # 4. 왼쪽 열: 아래 -> 위
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result