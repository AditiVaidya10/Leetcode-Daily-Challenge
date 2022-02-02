class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        aLen = len(p)
        counts = {i:p.count(i) for i in set(p)}
        res = []
        for i in range(len(s) - aLen + 1):
            snip = s[i:i + aLen]
            comp = {a:snip.count(a) for a in set(snip)}
            if counts == comp:
                res.append(i)
        return res
