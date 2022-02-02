# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.list = head
        e = []
        node = self.list 
        while (node):
            e.append(node.val)
            node = node.next
        self.e = e
        

    def getRandom(self) -> int:
        return random.choice(self.e)
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
