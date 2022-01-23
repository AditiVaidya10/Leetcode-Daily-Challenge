class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = collections.deque(list(range(1, 10)))
        res = []
        while queue:
            u = queue.popleft()
            if low <= u <= high :
                res.append(u)
            last_num = u % 10
            if last_num != 9:
                queue.append(u * 10 + last_num + 1)
        return res
