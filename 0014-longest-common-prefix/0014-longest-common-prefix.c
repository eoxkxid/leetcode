char* longestCommonPrefix(char** strs, int strsSize) {
    char* first_word = strs[0];

    for (int i = 0; first_word[i] != '\0'; i++) {
        char current_char = first_word[i];

        for (int j = 1; j < strsSize; j++) {
            /*
             * strs[j][i] == '\0' 이면
             * 현재 문자열이 first_word보다 짧아서 더 이상 공통 접두사가 될 수 없음
             * 
             * strs[j][i] != current_char이면
             * 같은 위치의 문자가 다르므로 공통 접두사가 바뀜
             */
            if (strs[j][i] == '\0' || strs[j][i] != current_char) {
                first_word[i] = '\0';
                return first_word;
            }
        }
    }

    return first_word;
}