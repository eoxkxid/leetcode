#include <stdbool.h>
#include <string.h>

bool isSubsequence(char* s, char* t) {
    int s_index = 0;
    int s_len = strlen(s);

    for (int i = 0; t[i] != '\0'; i++) {
        // s의 모든 문자를 이미 찾은 경우
        if (s_index == s_len) {
            return true;
        }

        // 현재 t의 문자가 s에서 필요한 문자와 같으면 다음 문자로 이동
        if (t[i] == s[s_index]) {
            s_index++;
        }
    }

    return s_index == s_len;
}