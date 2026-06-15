#include <stdbool.h>
#include <string.h>

bool isIsomorphic(char* s, char* t) {
    int s_to_t[256];
    int t_to_s[256];

    // 아직 매핑되지 않았다는 의미로 -1 초기화
    for (int i = 0; i < 256; i++) {
        s_to_t[i] = -1;
        t_to_s[i] = -1;
    }

    int length = strlen(s);

    for (int i = 0; i < length; i++) {
        unsigned char char_s = s[i];
        unsigned char char_t = t[i];

        // s의 문자가 이미 다른 t 문자로 매핑되어 있으면 실패
        if (s_to_t[char_s] != -1 && s_to_t[char_s] != char_t) {
            return false;
        }

        // t의 문자가 이미 다른 s 문자에서 온 적 있으면 실패
        if (t_to_s[char_t] != -1 && t_to_s[char_t] != char_s) {
            return false;
        }

        // 현재 문자 쌍의 매핑 저장
        s_to_t[char_s] = char_t;
        t_to_s[char_t] = char_s;
    }

    return true;
}