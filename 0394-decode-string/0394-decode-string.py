class Solution:
    def decodeString(self, s: str) -> str:
        def decode(index: int) -> tuple[str, int]:
            result = []
            repeat = 0

            while index < len(s):
                char = s[index]

                # 여러 자리 반복 횟수 처리
                if char.isdigit():
                    repeat = repeat * 10 + int(char)

                # 대괄호 내부를 재귀적으로 디코딩
                elif char == "[":
                    decoded_part, index = decode(index + 1)

                    result.append(decoded_part * repeat)
                    repeat = 0

                # 현재 재귀 단계 종료
                elif char == "]":
                    return "".join(result), index

                # 일반 알파벳
                else:
                    result.append(char)

                index += 1

            # 가장 바깥 함수는 ']'를 만나지 않고 문자열 끝에서 종료
            return "".join(result), index

        decoded_string, _ = decode(0)
        return decoded_string