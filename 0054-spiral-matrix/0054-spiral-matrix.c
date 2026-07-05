#include <stdlib.h>

int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    int rows = matrixSize;
    int cols = matrixColSize[0];

    *returnSize = rows * cols;

    int* result = (int*)malloc((*returnSize) * sizeof(int));
    int index = 0;

    int top = 0;
    int bottom = rows - 1;
    int left = 0;
    int right = cols - 1;

    while (top <= bottom && left <= right) {
        // 1. 위쪽 행: 왼쪽 -> 오른쪽
        for (int col = left; col <= right; col++) {
            result[index++] = matrix[top][col];
        }
        top++;

        // 2. 오른쪽 열: 위 -> 아래
        for (int row = top; row <= bottom; row++) {
            result[index++] = matrix[row][right];
        }
        right--;

        // 3. 아래쪽 행: 오른쪽 -> 왼쪽
        if (top <= bottom) {
            for (int col = right; col >= left; col--) {
                result[index++] = matrix[bottom][col];
            }
            bottom--;
        }

        // 4. 왼쪽 열: 아래 -> 위
        if (left <= right) {
            for (int row = bottom; row >= top; row--) {
                result[index++] = matrix[row][left];
            }
            left++;
        }
    }

    return result;
}