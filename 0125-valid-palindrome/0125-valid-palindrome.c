#include <stdbool.h>
#include <ctype.h>
#include <string.h>

bool isPalindrome(char* s) {
    int left = 0;
    int right = strlen(s) - 1;

    while (left < right) {
        // 왼쪽 포인터가 알파벳/숫자를 가리킬 때까지 이동
        while (left < right && !isalnum((unsigned char)s[left])) {
            left++;
        }

        // 오른쪽 포인터가 알파벳/숫자를 가리킬 때까지 이동
        while (left < right && !isalnum((unsigned char)s[right])) {
            right --;
        }

        // 대소문자를 무시하고 비교
        if (tolower((unsigned char)s[left]) != tolower((unsigned char)s[right])) {
            return false;
        }

        left++;
        right--;
    }

    return true;
}