class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa = UnionFind(n) # for Alice
        ufb = UnionFind(n) # for Bob
        
        ans = 0
        edges.sort(reverse=True) 
        for t, u, v in edges: 
            u, v = u-1, v-1
            if t == 3: ans += not (ufa.union(u, v) and ufb.union(u, v)) # Alice & Bob
            elif t == 2: ans += not ufb.union(u, v)                     # Bob only
            else: ans += not ufa.union(u, v)                            # Alice only
        return ans if ufa.count == 1 and ufb.count == 1 else -1 # check if uf is connected
