# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 빈 리스트이거나 노드가 하나뿐이면 회전해도 동일하다
        if head is None or head.next is None or k == 0:
            return head

        # 1. 리스트 길이와 기존 꼬리를 구한다
        length = 1
        tail = head

        while tail.next is not None:
            tail = tail.next
            length += 1

        # 2. 불필요한 회전을 제거한다
        k %= length

        # 리스트 길이의 배수만큼 회전하면 원래 리스트와 같다
        if k == 0:
            return head

        # 3. 기존 꼬리를 기존 head와 연결하여 원형 리스트로 만든다
        tail.next = head

        # 4. 새로운 꼬리를 찾는다
        # 새로운 꼬리의 인덱스는 length - k - 1이다
        new_tail = head

        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # 5. 새로운 머리를 저장한다
        new_head = new_tail.next

        # 6. 새로운 꼬리 뒤를 끊어 원형 리스트를 일반 리스트로 되돌린다
        new_tail.next = None

        return new_head