class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        # p가 s보다 길면 애너그램이 존재할 수 없다
        if len(p) > len(s):
            return result

        p_count = [0] * 26
        window_count = [0] * 26

        # p의 문자 빈도 계산
        for char in p:
            p_count[ord(char) - ord('a')] += 1

        left = 0
        p_len = len(p)

        for right in range(len(s)):
            # 오른쪽 문자 추가
            right_index = ord(s[right]) - ord('a')
            window_count[right_index] += 1

            # 윈도우 크기가 p_len보다 커지면 왼쪽 문자 제거
            if right - left + 1 > p_len:
                left_index = ord(s[left]) - ord('a')
                window_count[left_index] -= 1
                left += 1

            # 윈도우 크기가 p_len이고 문자 빈도가 같으면 애너그램
            if right - left + 1 == p_len and window_count == p_count:
                result.append(left)

        return result