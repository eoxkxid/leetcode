class Solution:
    def decodeString(self, s: str) -> str:
        index = 0

        def decode() -> str:
            nonlocal index

            decoded_parts = []

            # 현재 깊이의 문자열을 해석한다.
            # ']'를 만나면 현재 재귀 호출의 작업이 끝난다.
            while index < len(s) and s[index] != "]":

                # 일반 알파벳은 결과에 그대로 추가한다.
                if s[index].isalpha():
                    decoded_parts.append(s[index])
                    index += 1

                # 숫자가 나오면 반드시 k[encoded_string] 구조가 시작된다.
                else:
                    repeat_count = 0

                    # 반복횟수는 여라 자리일 수 있다.
                    while index < len(s) and s[index].isdigit():
                        repeat_count = (
                            repeat_count * 10 + int(s[index])
                        )
                        index += 1

                    # 현재 위치는 '['이므로 건너뛴다.
                    index += 1

                    # '[' 안쪽 문자열을 재귀적으로 해석한다.
                    nested_string = decode()

                    # 재귀 함수가 종료되었을 때 현재 위치는 ']'다.
                    # ']'를 건너뛰고 다음 문자로 이동한다.
                    index += 1

                    # 내부 문자열을 repeat_count번 반복한다.
                    decoded_parts.append(
                        nested_string * repeat_count
                    )

            return "".join(decoded_parts)

        return decode()