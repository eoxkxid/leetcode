from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]

        for i in range(len(first_word)):
            current_char = first_word[i]

            for word in strs[1:]:
                # i가 word의 길이 이상이면 해당 위치의 문자가 존재하지 않음
                if i >= len(word):
                    return first_word[:i]

                # 같은 위치의 문자가 다르면 공통 접두사는 여기서 끝남
                if word[i] != current_char:
                    return first_word[:i]

        return first_word