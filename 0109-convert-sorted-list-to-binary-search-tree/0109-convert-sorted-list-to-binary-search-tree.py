# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(
        self,
        head: Optional[ListNode]
    ) -> Optional[TreeNode]:

        # 빈 연결 리스트는 빈 트리가 된다.
        if head is None:
            return None

        # 노드가 하나뿐이면 그 노드가 리프 노드가 된다.
        if head.next is None:
            return TreeNode(head.val)

        previous = None
        slow = head
        fast = head

        # slow는 한 칸, fast는 두 칸씩 이동한다.
        # 반복이 끝나면 slow가 가운데 노드를 가리킨다.
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        # 가운데 노드 이전에서 연결을 끊어
        # 왼쪽 연결 리스트를 독립시킨다.
        previous.next = None

        # 가운데 노드를 현재 서브트리의 루트로 사용한다.
        root = TreeNode(slow.val)

        # 가운데 노드 왼쪽 부분으로 왼쪽 서브트리를 만든다.
        root.left = self.sortedListToBST(head)

        # 가운데 노드 오른쪽 부분으로 오른쪽 서브트리를 만든다.
        root.right = self.sortedListToBST(slow.next)

        return root