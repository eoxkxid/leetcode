class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        # 1. 첫 번째 행에 0이 있는지 확인
        first_row_has_zero = False
        for col in range(cols):
            if matrix[0][col] == 0:
                first_row_has_zero = True
                break

        # 2. 첫 번째 열에 0이 있는지 확인
        first_col_has_zero = False
        for row in range(rows):
            if matrix[row][0] == 0:
                first_col_has_zero = True
                break

        # 3. 내부 영역에서 0을 찾고, 첫 행/첫 열에 마킹
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # 4. 마커를 보고 내부 영역을 0으로 변경
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # 5. 원래 첫 번째 행에 0이 있었다면 첫 번째 행 전체를 0으로 변경
        if first_row_has_zero:
            for col in range(cols):
                matrix[0][col] = 0

        # 6. 원래 첫 번째 열에 0이 있었다면 첫 번째 열 전체를 0으로 변경
        if first_col_has_zero:
            for row in range(rows):
                matrix[row][0] = 0