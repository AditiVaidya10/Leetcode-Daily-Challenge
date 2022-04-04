# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        first = fast = second = head
        for i in range(1, k):
            fast = fast.next
        first = fast
        while fast.next:
            fast = fast.next
            second = second.next
        first.val, second.val = second.val, first.val
        return head
