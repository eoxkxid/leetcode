class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        # s1이 s2보다 길면, s2 안에 s1의 순열이 들어갈 수 없다
        if window_size > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        # s1의 빈도수와 s2의 첫 윈도우 빈도수 계산
        for i in range(window_size):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # 첫 윈도우 확인
        if s1_count == window_count:
            return True

        # 윈도우를 오른쪽으로 한 칸씩 이동
        for right in range(window_size, len(s2)):
            left = right - window_size

            # 새로 들어오는 문자 추가
            window_count[ord(s2[right]) - ord('a')] += 1

            # 윈도우에서 빠지는 문자 제거
            window_count[ord(s2[left]) - ord('a')] -= 1

            # 현재 윈도우가 s1의 순열인지 확인
            if s1_count == window_count:
                return True

        return False 
