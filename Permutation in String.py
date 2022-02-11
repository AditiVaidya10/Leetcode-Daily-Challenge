class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        end = len(s1)
        i = 0
        while end <= len(s2):
            if s1 == sorted(s2[i:end]):
                return True
            i += 1
            end += 1
        return False
