class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        path = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        def backtrack(start):
            # 문자열 전체를 성공적으로 partition한 경우
            if start == len(s):
                result.append(path[:])
                return

            # s[start:end+1]을 현재 substring으로 선택해 본다.
            for end in range(start, len(s)):

                # palindrome이 아니라면 선택할 수 없다.
                if not is_palindrome(start, end):
                    continue

                # 선택
                path.append(s[start:end + 1])

                # 다음 위치부터 탐색
                backtrack(end + 1)

                # 선택 취소
                path.pop()

        backtrack(0)

        return result