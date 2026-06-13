class Solution:
    def reverseWords(self, s: str) -> str:
        # split()은 앞뒤 공백과 여러 개의 연속 공백을 자동으로 무시하고 단어만 분리한다.
        words = s.split()

        # 단어 순서를 뒤집은 뒤, 공백 하나로 연결한다.
        return " ".join(words[::-1])

    # 더 짧은 코드
    # return " ".join(s.split()[::-1])
        