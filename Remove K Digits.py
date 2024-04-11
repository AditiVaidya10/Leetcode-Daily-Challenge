class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        # Iterate through each digit in num
        for digit in num:
            # While there are digits in the stack, k > 0, and the current digit is smaller than the top of the stack
            while k > 0 and stack and stack[-1] > digit:
                # Remove the top of the stack
                stack.pop()
                k -= 1
            # Append the current digit to the stack
            stack.append(digit)
        
        # If there are still digits left to remove, remove them from the end of the stack
        while k > 0:
            stack.pop()
            k -= 1
        
        # Remove leading zeros
        while stack and stack[0] == '0':
            stack.pop(0)
        
        # If stack is empty, return '0', otherwise, return the concatenated stack as a string
        return ''.join(stack) if stack else '0'
