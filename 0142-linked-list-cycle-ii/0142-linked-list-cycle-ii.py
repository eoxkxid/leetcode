# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional:
        slow = head
        fast = head

        # 1. 사이클 존재 여부 확인
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        else:
            # fast가 None에 도달했다면 사이클이 없음
            return None

        # 2. 사이클의 시작점 탐색
        finder = head

        while finder is not slow:
            finder = finder.next
            slow = slow.next

        return finder