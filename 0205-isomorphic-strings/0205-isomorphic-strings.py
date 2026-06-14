class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # s의 문자가 이미 다른 t 문자로 매핑된 경우
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False

            # t의 문자가 이미 다른 s 문자에서 온 경우
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False

            # 현재 매핑 저장
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True            
        