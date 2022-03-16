class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(pushed)
        i = 0
        j = 0
        while i <= n and j < n:
            while len(stack) == 0 or stack[-1] != popped[j] and i < n and j < n:
                stack.append(pushed[i])
                i += 1
            
            if stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                return False
        
        return stack == []
