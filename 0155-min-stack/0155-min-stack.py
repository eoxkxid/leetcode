class MinStack:

    def __init__(self):
        # 각 원소를 (실제 값, 현재까지의 최솟값) 형태로 저장
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            # 첫 번째 원소는 그 자체가 최솟값
            current_min = val
        else:
            # 기존 최솟값과 새로운 값을 비교
            previous_min = self.stack[-1][1]
            current_min = min(val, previous_min)

        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        # 튜플의 첫 번째 값이 실제 스택 원소
        return self.stack[-1][0]

    def getMin(self) -> int:
        # 튜플의 두 번째 값이 현재 스택의 최솟값
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()