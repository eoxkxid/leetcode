class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0

        for char in t:
            # s의 모든 문자를 이미 찾은 경우
            if s_index == len(s):
                return True

            # 현재 t의 문자가 s에서 필요한 문자와 같다면 다음 문자로 이동
            if char == s[s_index]:
                s_index += 1

        # t를 모두 확인한 뒤 s 전체를 찾았는지 확인
        return s_index == len(s)