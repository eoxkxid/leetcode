# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # list1이 끝났다면 list2의 남은 부분을 그대로 연결
        if list1 is None:
            return list2

        # list2가 끝났다면 list1의 남은 부분을 그대로 연결
        if list2 is None:
            return list1

        # list1의 현재 값이 더 작거나 같은 경우
        if list1.val <= list2.val:
            # list1을 현재 노드로 선택하고,
            # 그 뒤에는 list1의 다음 노드와 list2를 병합한 결과를 연결
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
            
        # list2의 현재 값이 더 작은 경우
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2