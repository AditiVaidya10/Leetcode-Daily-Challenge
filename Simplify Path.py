class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        str_arr = path.split('/')
        
        for char in str_arr:
            
            if not char or char == '.':
                continue
            
            elif char == '..':
                if res:
                    res.pop()
                
            else:
                res.append(char)
                
                
        return '/' + '/'.join(res)
