# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 첫 번쨰 노드도 일반적인 방식으로 처리하기 위한 더미 노드
        dummy = ListNode(0, head)

        # 현재 교환할 두 노드의 바로 앞 노드
        prev = dummy

        # 교환할 노드가 두 개 이상 남아 있는 동안 반복
        while prev.next is not None and prev.next.next is not None:
            first = prev.next
            second = first.next

            # prev -> first -> second -> next_pair
            # prev -> second -> first -> next_pair 로 변경
            first.next = second.next
            second.next = first
            prev.next = second

            # 다음 쌍을 처리하기 위해 이동
            prev = first

        return dummy.next