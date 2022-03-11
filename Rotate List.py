class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        k = k % size if size else 0
        if size <= 1 or k == 0:
            return head
        slow, fast = head, head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        res = cur = slow.next
        while cur and cur.next:
            cur = cur.next
        cur.next = head
        slow.next = None
        return res
