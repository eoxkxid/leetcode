class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        # 아직 더 따뜻한 날을 찾지 못한 날짜의 인덱스 저장
        stack = []

        for current_index, current_temperature in enumerate(temperatures):

            # 현재 날짜가 스택 맨 위 날짜보다 더 따뜻한 경우
            while (
                stack
                and temperatures[stack[-1]] < current_temperature
            ):
                previous_index = stack.pop()

                # 두 날짜 사이의 거리 계산
                answer[previous_index] = current_index - previous_index

            # 현재 날짜도 이후의 더 따뜻한 날을 기다림
            stack.append(current_index)

        return answer