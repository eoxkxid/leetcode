# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # fast가 두 칸 이동할 수 있는 동안 반복
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow