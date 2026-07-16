# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 결과 연결 리스트의 시작을 편리하게 관리하기 위한 더미 노드
        dummy = ListNode()
        current = dummy

        carry = 0
        
        # 두 리스트 또는 자리올림 중 하나라도 남아 있으면 계속 계산
        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            total = value1 + value2 + carry

            # total을 10으로 나눈 몫과 나머지
            carry, digit = divmod(total, 10)

            # 현재 결과 자릿수를 새로운 노드로 추가
            current.next = ListNode(digit)
            current = current.next

            # 현재 노드가 존재하면 다음 노드로 이동
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
            
        # dummy 자체는 실제 결과가 아니므로 dummy.next 반환
        return dummy.next