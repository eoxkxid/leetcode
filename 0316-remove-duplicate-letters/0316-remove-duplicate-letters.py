class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 각 문자가 앞으로 몇 번 더 등장하는지 기록
        remaining_count = Counter(s)

        # 최종 문자열을 구성하는 스택
        stack = []

        # 특정 문자가 이미 스택에 들어 있는지 기록
        in_stack = set()

        for char in s:
            # 현재 문자를 처리했으므로 남은 개수 감소
            remaining_count[char] -= 1

            # 이미 결과에 포함된 문자는 다시 넣지 않음
            if char in in_stack:
                continue

            # 현재 문자보다 크고, 뒤에서 다시 등장하는 문자 제거
            while (
                stack
                and stack[-1] > char
                and remaining_count[stack[-1]] > 0
            ):
                removed_char = stack.pop()
                in_stack.remove(removed_char)

            stack.append(char)
            in_stack.add(char)

        return "".join(stack)