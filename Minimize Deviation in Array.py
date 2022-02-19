class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        import heapq
        ans = float('inf')
        heap = [-(x*2) if x%2 else -x for x in nums]; heapq.heapify(heap)
        mini = -max(heap)
        while not heap[0] % 2:
            curr = -heapq.heappop(heap)
            ans = min(ans, curr-mini)
            mini = min(mini, curr//2)
            if not curr%2: heapq.heappush(heap, -(curr//2))
        ans = min(ans, -heap[0] -mini)
        return ans
