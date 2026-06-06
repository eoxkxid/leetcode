#include <stdint.h>

int hammingWeight(int n) {
    int count = 0;

    while(n) {
        // 가장 오른쪽 비트가 1인지 확인
        if (n & 1) {
            count++;
        }

        // 오른쪽으로 한 칸 shift
        n >>= 1;
    }

    return count;
}