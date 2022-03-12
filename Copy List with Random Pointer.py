"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        d = {}
        prev, cur = None, head
        while cur:
            d[cur] = copy.copy(cur)
            if prev:
                d[prev].next = d[cur]
            
            prev, cur =cur, cur.next
        cur = head
        while cur:
            if cur.random:
                d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]
