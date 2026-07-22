class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closing_to_opening = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for bracket in s:
            # 닫는 괄호인 경우
            if bracket in closing_to_opening:
                # 대응할 여는 괄호가 없거나 종류가 다르면 유효하지 않음
                if not stack or stack[-1] != closing_to_opening[bracket]:
                    return False

                stack.pop()

            # 여는 괄호인 경우
            else:
                stack.append(bracket)

        # 닫히지 않은 여는 괄호가 남아 있으면 Flase
        return not stack