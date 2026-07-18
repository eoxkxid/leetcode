# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current is not None:
            # 현재 연결을 바꾸기 전에 다음 노드를 저장
            next_node = current.next

            # 현재 노드가 이전 노드를 가리키도록 방향 변경
            current.next = previous

            # 두 포인터를 한 칸씩 앞으로 이동
            previous = current
            current = next_node
    
        # 반복 종료 후 previous가 새로운 head
        return previous