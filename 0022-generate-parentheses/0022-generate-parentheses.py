class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []

        def backtrack(open_count, close_count):
            # n쌍의 괄호를 모두 사용한 경우
            if open_count == n and close_count == n:
                result.append("".join(current))
                return

            # 여는 괄호는 최대 n개까지 사용 가능
            if open_count < n:
                current.append("(")
                backtrack(open_count + 1, close_count)
                current.pop()  # 선택 되돌리기

            # 닫는 괄호는 사용한 여는 괄호보다 적을 때만 추가 가능
            if close_count < open_count:
                current.append(")")
                backtrack(open_count, close_count + 1)
                current.pop()  # 선택 되돌리기

        backtrack(0, 0)

        return result