# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        lst = []
        while(head):
            lst.append(head.val)
            head = head.next
        h = tmp = ListNode(0)
        lst = sorted(lst)
        for i in lst:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return h.next
