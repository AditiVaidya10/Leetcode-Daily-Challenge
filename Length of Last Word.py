class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if len(words) == 0:
            return 0
        return len(words[-1])

"""
Leetcode Discussion Link :- https://leetcode.com/problems/length-of-last-word/solutions/4955805/length-of-last-word-solution-in-python/?envType=daily-question&envId=2024-04-01
"""
