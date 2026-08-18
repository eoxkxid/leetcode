# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 빈 리스트 또는 노드가 하나뿐이면 이미 정렬된 상태다.
        if head is None or head.next is None:
            return head

        # 1. slow/fast 포인터로 리스트의 중간 지점을 찾는다.
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 리스트를 왼쪽과 오른쪽으로 실제로 분리한다.
        right_head = slow.next
        slow.next = None

        # 3. 각 부분을 재귀적으로 정렬한다.
        left = self.sortList(head)
        right = self.sortList(right_head)

        # 4. 정렬된 두 리스트를 병합한다.
        return self.merge(left, right)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        # 두 리스트의 현재 노드 중 더 작은 노드를 연결한다.
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # 한쪽 리스트가 먼저 끝나면 나머지 리스트를 그대로 연결한다.
        current.next = left if left else right

        return dummy.next