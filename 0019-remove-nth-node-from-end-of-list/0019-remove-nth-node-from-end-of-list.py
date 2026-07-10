# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 맨 앞 노드 삭제도 동일하게 처리하기 위한 가상 노드
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # slow가 삭제 대상의 이전 노드에 멈추도록
        # fast를 n칸 먼저 이동
        for _ in range(n):
            fast = fast.next

        # fast가 리스트 끝을 넘어갈 때까지 함께 이동
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # slow.next가 삭제 대상 노드
        slow.next = slow.next.next

        return dummy.next