class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        mapping_s_to_t = {}
        mapping_t_to_s = {}
    
        for char_s, char_t in zip(s, t):
            if char_s not in mapping_s_to_t and char_t not in mapping_t_to_s:
                mapping_s_to_t[char_s] = char_t
                mapping_t_to_s[char_t] = char_s
            elif mapping_s_to_t.get(char_s) != char_t or mapping_t_to_s.get(char_t) != char_s:
                return False
        
        return True
