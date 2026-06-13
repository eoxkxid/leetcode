#include <string.h>

void reverse(char* s, int left, int right) {
    while (left < right) {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left++;
        right--;
    }
}

char* reverseWords(char* s) {
    int n = strlen(s);

    // 1. 전체 문자열 뒤집기
    reverse(s, 0, n - 1);

    // 2. 각 단어를 다시 뒤집기
    int start = 0;
    for (int end = 0; end <= n; end++) {
        if (s[end] == ' ' || s[end] == '\0') {
            reverse(s, start, end - 1);
            start = end + 1;
        }
    }

    // 3. 공백 정리
    int read = 0;
    int write = 0;

    while (s[read] != '\0') {
        // 연속 공백 스킵
        while (s[read] == ' ') {
            read++;
        }

        // 단어를 찾았고, 이미 앞에 단어가 있다면 공백 하나 추가
        if (s[read] != '\0') {
            if (write > 0 ) {
                s[write++] = ' ';
            }

            // 단어 복사
            while (s[read] != '\0' && s[read] != ' ') {
                s[write++] = s[read++];
            }
        }
    }

    // 문자열 종료 문자
    s[write] = '\0';

    return s;
}