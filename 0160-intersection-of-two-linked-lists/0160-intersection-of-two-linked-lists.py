# LeetCode에서 제공하는 노드 정의
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer_a = headA
        pointer_b = headB

        # 같은 노드 객체를 가리킬 때까지 이동한다.
        while pointer_a is not pointer_b:
            # A의 끝에 도달하면 B의 시작점으로 이동한다.
            if pointer_a is None:
                pointer_a = headB
            else:
                pointer_a = pointer_a.next

            # B의 끝에 도달하면 A의 시작점으로 이동한다.
            if pointer_b is None:
                pointer_b = headA
            else:
                pointer_b = pointer_b.next

        # 교차점이 있으면 해당 노드,
        # 교차점이 없으면 None이다.
        return pointer_a