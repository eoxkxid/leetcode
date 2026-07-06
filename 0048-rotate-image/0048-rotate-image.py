class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 1. 전치: matrix[i][j] <-> matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        # 2. 각 행을 뒤집기
        for row in matrix:
            row.reverse()