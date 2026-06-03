class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # 왼쪽 포인터가 알파벳/숫자를 가리킬 때까지 이동
            while left < right and not s[left].isalnum():
                left += 1

            # 오른쪽 포인터가 알파벳/숫자를 가리킬 때까지 이동
            while left < right and not s[right].isalnum():
                right -= 1

            # 대소문자를 무시하고 비교
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True        